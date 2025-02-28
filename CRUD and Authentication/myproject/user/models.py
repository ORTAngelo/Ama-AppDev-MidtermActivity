from django.db import models

# Create your models here.
class Product(models.Model):
    serial_number = models.CharField(max_length=50)
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name