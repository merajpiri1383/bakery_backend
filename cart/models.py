from django.db import models
from django.contrib.auth import get_user_model
from django_jalali.db.models import jDateTimeField
from product.models import Product
class Cart(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="carts")
    created = jDateTimeField(auto_now_add=True)
    is_open = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    def __str__(self):
        return f"Cart : {self.user} "
class CartProduct(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="cart_products")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"Cart Product -- {self.cart} > {self.product}"