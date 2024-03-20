from django.db import models
from django_jalali.db.models import jDateTimeField
class Category(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="categories")
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="products")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    price = models.PositiveIntegerField()
    created = jDateTimeField(auto_now_add=True)
    updated = jDateTimeField(auto_now=True)
    def __str__(self):
        return self.name