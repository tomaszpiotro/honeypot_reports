from django.db import models


class FrequentItemSetQuerySet(models.QuerySet):
    def between_dates(self, upper_date, lower_date):
        return self.filter(operation__start__lte=upper_date,
                           operation__end__gte=lower_date)


class FrequentItemSetManager(models.Manager):
    def get_queryset(self):
        return FrequentItemSetQuerySet(self.model, using='miner')
