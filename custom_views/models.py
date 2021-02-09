from django.db import models


class AnalyticsModel(models.Model):

    name = models.CharField(max_length=127, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Analytics Report'
