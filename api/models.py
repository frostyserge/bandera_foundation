from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User



# class Order(models.Model):
#     payment_method = models.CharField()

class Merch(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # SET_NULL means that if a user gets deleted the products that it is connected to will remain in the database
    name = models.CharField(max_length=200, null=True, blank=True)
    img = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock_amount = models.IntegerField(null=True, blank=True, default=0)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False, default=None)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Event(models.Model):
    name = models.CharField(max_length=150)
    img = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    location = models.CharField(max_length=500)
    time_and_date = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

class Project(models.Model):
    name = models.CharField(max_length=150)
    img = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    goal = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

