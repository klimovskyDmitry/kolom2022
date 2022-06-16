from django.db import models

class Auto (models.Model):
    id = models.IntegerField (primary_key=True)
    gar = models.PositiveSmallIntegerField (verbose_name='Гар.№')
    title = models.CharField (verbose_name='Марка, модель', max_length=100)
    type = models.CharField (verbose_name='Тип', max_length=100)
