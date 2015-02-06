from django.db import models

from miner.models import FrequentItemSet


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


class ReportItem(models.Model):
    frequent_item_set = models.ForeignKey(
        FrequentItemSet,
        verbose_name="frequent item sets",
        null=True
    )
    one_hour_occurrences = models.IntegerField(
        verbose_name="one hour window occurrences"
    )
    two_hour_occurrences = models.IntegerField(
        verbose_name="two hours window occurrences"
    )
    four_hour_occurrences = models.IntegerField(
        verbose_name="four hours window occurrences"
    )
    eight_hour_occurrences = models.IntegerField(
        verbose_name="eight hours window occurrences"
    )
    sixteen_hour_occurrences = models.IntegerField(
        verbose_name="sixteen hours window occurrences"
    )
    total_occurrences = models.IntegerField(
        verbose_name="total previous occurrences"
    )
    report = models.ForeignKey(
        Report,
        verbose_name="report"
    )

    def is_seen_before(self):
        occurrences = [self.one_hour_occurrences, self.two_hour_occurrences,
                       self.four_hour_occurrences, self.eight_hour_occurrences,
                       self.sixteen_hour_occurrences]
        return any([occurrence > 0 for occurrence in occurrences])
