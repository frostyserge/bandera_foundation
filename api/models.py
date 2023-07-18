from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User




class Merch(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # SET_NULL means that if a user gets deleted the products that it is connected to will remain in the database
    name = models.CharField(max_length=200, null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock_amount = models.IntegerField(null=True, blank=True, default=0)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False, default=None)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    payment_method = models.CharField()
    tax_cost = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    shipping_cost = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    total_cost = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    is_delivered = models.BooleanField(default=False)
    delivered_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.created_at)
    
class OrderItem(models.Model):
    merch_item = models.ForeignKey(Merch, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=500, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name
    
class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=500, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True, default=0)
    country = models.CharField(max_length=500, null=True, blank=True)
    shipping_cost = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.address

class Event(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    img = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=500)
    time_and_date = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

class Project(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    img = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    goal = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

