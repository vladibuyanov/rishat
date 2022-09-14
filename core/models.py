from django.db import models


class Item(models.Model):
    """ Модель Item """
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Модель Item'
        verbose_name_plural = 'Модель Items'

    def __str__(self):
        return self.name
