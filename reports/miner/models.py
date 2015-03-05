from django.db import models

from .frequent_item_set_manager import FrequentItemSetManager
from .operations_manager import OperationManager


class SaveNotAllowedException(Exception):
    pass


class SaveNotAllowedModel(models.Model):
    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        raise SaveNotAllowedException


class Operation(SaveNotAllowedModel):
    start = models.DateTimeField(
        verbose_name="operation start time",
        db_column="start_time"
    )
    end = models.DateTimeField(
        verbose_name="operation end time",
        db_column="end_time"
    )
    minimal_sup = models.SmallIntegerField(
        verbose_name="not used",
        db_column="minsup"
    )
    interval = models.IntegerField(
        verbose_name="time interval in seconds",
        db_column="interval"
    )
    request_id = models.IntegerField(
        verbose_name="not used"
    )
    tag = models.CharField(
        max_length=32,
        verbose_name="operation tag"
    )

    _base_manager = models.Manager()
    objects = OperationManager()

    class Meta:
        db_table = u'operations'

    def __str__(self):
        return str(self.id) + " " + str(self.start) + " " + str(self.end)


class FrequentItemSet(SaveNotAllowedModel):
    operation = models.ForeignKey(
        Operation,
        verbose_name="operation",
        db_column='oid',
        related_name='item_set'
    )
    protocol = models.CharField(
        max_length=32,
        verbose_name="protocol"
    )
    remote_host = models.IPAddressField(
        verbose_name="remote host"
    )
    remote_port = models.IntegerField(
        verbose_name="remote port"
    )
    local_host = models.IPAddressField(
        verbose_name="local host"
    )
    local_port = models.IntegerField(
        verbose_name="local port"
    )
    count = models.IntegerField(
        verbose_name="count"
    )
    generator = models.BooleanField(
        default=False,
        verbose_name="defines whether item set is generated or not"
    )
    jep = models.BooleanField(
        default=False,
        db_column="ejp"
    )
    interesting = models.BooleanField(
        default=False
    )

    _base_manager = models.Manager()
    objects = FrequentItemSetManager()

    class Meta:
        db_table = u'freq_itemsets'

    def __str__(self):
        return (str(self.id) + " " + str(self.protocol) + " "
                + str(self.remote_host) + " " + str(self.remote_port) + " "
                + str(self.local_port) + " " + str(self.count))

    def is_between_dates(self, upper_date, lower_date):
        return upper_date >= self.operation.start >= lower_date
