from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
from .servises import StripeManager


class Item(models.Model):

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=11, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    product_stripe_id = models.CharField(max_length=50, blank=True)
    price_stripe_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item', args=[self.pk])

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
            self.product_stripe_id = StripeManager.create_product_and_return_id(self.pk)
            self.price_stripe_id = StripeManager.create_price_and_return_id(self)
            super().save(*args, **kwargs)
