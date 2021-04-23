from django.db import models

# Create your models here.

class Dish(models.Model):
    name = models.CharField(max_length = 255)
    price = models.IntegerField()

    class Meta:
        verbose_name = 'блюдо'
        verbose_name_plural = 'Блюдо'

    def __str__(self):
        return self.name
