from django.db import models, transaction
from django.db.models.query import QuerySet

from miner.models import FrequentItemSet, Operation

import datetime
import pytz


def _find_same_items(item, operations):
    frequent_item_sets = []
    print "operations " + str(len(operations))
    for operation in operations:
        print operation
        sets = operation.item_set.all().filter(
            generator=False, protocol=item.protocol,
            remote_host=item.remote_host, remote_port=item.remote_port,
            local_host=item.local_host, count=item.count,
            )
        frequent_item_sets += sets
    return frequent_item_sets


class ReportQuerySet(QuerySet):
    pass


class ReportManager(models.Manager):
    def get_queryset(self):
        return ReportQuerySet(self.model, using='default')

    @transaction.atomic
    def create(self, interval,
               start_time=datetime.datetime.now(pytz.utc).replace(
                   minute=0, second=0, microsecond=0), **kwargs):
        end_time = start_time - datetime.timedelta(hours=interval)
        kwargs.update({'start_time': start_time, 'end_time': end_time})
        print "#######"
        report = super(ReportManager, self).create(**kwargs)
        print "@@@@@@@"
        print "start " + str(start_time)
        print "end " + str(end_time)

        operations = Operation.objects.all().between_dates(
            upper_date=start_time, lower_date=end_time)
        frequent_item_sets = FrequentItemSet.objects.filter(
            operation__in=operations,
            generator=False)
        print "freq " + str(len(frequent_item_sets))
        for item in frequent_item_sets:
            print item
            one_hour_occurrences = 0
            # other_operations = Operation.objects. \
            #     filter(start__lte=end_time)
            # itemsets = _find_same_items(
            #     item=item, operations=other_operations)

            itemsets = FrequentItemSet.objects.filter(
                generator=False, protocol=item.protocol,
                remote_host=item.remote_host, remote_port=item.remote_port,
                local_host=item.local_host, count=item.count,
                operation__start__lte=end_time)
            report_item = ReportItem.objects.create(
                frequent_item_set=item.id, report=report)
            end_date = Operation.objects.first().end
            delta = datetime.timedelta(hours=1)
            date = end_time
            while date > end_date:
                date2 = date - delta
                l = [itemset.is_between_dates(date, date2)
                     for itemset in itemsets]
                if any(l):
                    one_hour_occurrences += 1
                date -= delta
            report_item.one_hour_occurrences = one_hour_occurrences
            print " finished date processing "
            report_item.save()

        return report


class Report(models.Model):
    creation_date = models.DateTimeField(
        verbose_name="report creation date",
        auto_now_add=True
    )
    start_time = models.DateTimeField(
        verbose_name="Upper time bracket"
    )
    end_time = models.DateTimeField(
        verbose_name="Lower time bracket"
    )

    objects = ReportManager()

    def get_occurrences_number(self):
        return self.items.all().count()

    def get_new_occurrences_number(self):
        return self.items.filter(one_hour_occurrences__gt=0).count()


class ReportItem(models.Model):
    frequent_item_set = models.IntegerField(
        verbose_name="frequent item sets",
        null=True
    )
    one_hour_occurrences = models.IntegerField(
        verbose_name="one hour window occurrences",
        default=0
    )
    two_hour_occurrences = models.IntegerField(
        verbose_name="two hours window occurrences",
        default=0
    )
    four_hour_occurrences = models.IntegerField(
        verbose_name="four hours window occurrences",
        default=0
    )
    eight_hour_occurrences = models.IntegerField(
        verbose_name="eight hours window occurrences",
        default=0
    )
    sixteen_hour_occurrences = models.IntegerField(
        verbose_name="sixteen hours window occurrences",
        default=0
    )
    total_occurrences = models.IntegerField(
        verbose_name="total previous occurrences",
        default=0
    )
    report = models.ForeignKey(
        Report,
        verbose_name="report",
        null=True,  # TODO REMOVE
        blank=True,
        related_name='items'
    )

    def is_seen_before(self):
        return self.one_hour_occurrences > 0
