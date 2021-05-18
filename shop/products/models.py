from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()

    @staticmethod
    def product_count():
        return Product.objects.count()

    def __str__(self):
        return self.name
