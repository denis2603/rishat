from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator


class Item(models.Model):

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=11, decimal_places=2, default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item', args=[self.pk])
