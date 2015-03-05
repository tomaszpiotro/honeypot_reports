from django.db import models


class OperationQuerySet(models.QuerySet):
    def between_dates(self, upper_date, lower_date):
        return self.filter(start__lte=upper_date,
                           start__gte=lower_date)


class OperationManager(models.Manager):
    def get_queryset(self):
        return OperationQuerySet(self.model, using='miner')
