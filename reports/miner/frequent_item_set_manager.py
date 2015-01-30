from django.db import models


class FrequentItemSetQuerySet(models.QuerySet):
    pass


class FrequentItemSetManager(models.Manager):
    def get_queryset(self):
        return FrequentItemSetQuerySet(self.model, using='miner')
