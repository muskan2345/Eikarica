from collections import ChainMap
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, default='null')
    password = models.CharField(max_length=15)
    #rpassword=models.CharField(max_length=15,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE)

    USERNAME_FIELD = 'name'

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_balance(self):
        items = self.items.filter(vendor_paid=False, order__vendors__in=[self.id])
        return sum((item.product.price * item.quantity) for item in items)
    
    def get_paid_amount(self):
        items = self.items.filter(vendor_paid=True, order__vendors__in=[self.id])
        return sum((item.product.price * item.quantity) for item in items)

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, default='null')
    password = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='customer', on_delete=models.CASCADE)
    

    USERNAME_FIELD='name'

    class Meta:
        ordering=['name']

    def __str__(self):
        return self.name    

