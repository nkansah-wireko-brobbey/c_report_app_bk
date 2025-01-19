from django.db import models
import uuid

# Create your models here.


class Employee(models.Model):
    employee_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
        max_length=225, 
        blank=False, 
        null=False
    )

    def __self__(self):
        return self.name

class Phone(models.Model):
    phone_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    brand = models.CharField(
        max_length=500
    )
    model = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=12,decimal_places=2)
    quantity = models.PositiveBigIntegerField()

    def  __str__(self):
        return self.brand  +" "+ self.model

class Shipping(models.Model):
    shipping_id  = models.UUIDField(
        primary_key=True,
        default = uuid.uuid4,
        blank= False,
        null  = False
    )
    phone  = models.ForeignKey(Phone, on_delete=models.PROTECT)
    shipped_date = models.DateField()
    quantity = models.IntegerField()
    destination = models.CharField(max_length=100)

class Receiving(models.Model):
    receiving_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        blank=False
    )
    phone = models.ForeignKey(Phone, on_delete= models.PROTECT)
    received_date = models.DateField(auto_now=True)

