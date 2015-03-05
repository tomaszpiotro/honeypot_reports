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
        verbose_name="report"
    )

    def is_seen_before(self):
        return self.one_hour_occurrences > 0
