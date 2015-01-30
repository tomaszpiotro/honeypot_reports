from django.db import models


class OperationQuerySet(models.QuerySet):
    pass


class OperationManager(models.Manager):
    def get_queryset(self):
        return OperationQuerySet(self.model, using='miner')
