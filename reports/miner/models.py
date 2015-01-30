from django.db import models


class Operation(models.Model):
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

    class Meta:
        db_table = u'operations'


class FrequentItemSet(models.Model):
    operation = models.ForeignKey(
        Operation,
        verbose_name="operation",
        db_column='oid'
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

    class Meta:
        db_table = u'freq_itemsets'
