from django.contrib.auth.models import User
from django.db import models

from Store.validators import validate_nonzero


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    email = models.EmailField(max_length=200)
    street_name = models.CharField(max_length=200)
    house_number = models.CharField(max_length=10)  # Chosen for a CharField because the number could be 120B
    postal_code = models.CharField(max_length=10)   # Chosen for a CharField because of dutch like postal_codes 4332LK

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Products(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.TextField(max_length=500, default="This is the product's description.")
    price = models.DecimalField(decimal_places=2, max_digits=6)
    ean = models.CharField(max_length=200)
    stock = models.PositiveIntegerField(validators=[validate_nonzero])

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.product_name


class Orders(models.Model):
    order_id = models.CharField(max_length=9, default='IO')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.order_id
