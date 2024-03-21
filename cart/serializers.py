from rest_framework import serializers 
from cart.models import CartProduct,Cart
from product.serializers import ProductMiniSerializer
from user.serializers import UserSerializer
class CartProductSerializer(serializers.ModelSerializer):
    product = ProductMiniSerializer(read_only=True)
    class Meta : 
        model = CartProduct
        fields = ["id","cart","product","count"]
class CartSerializer(serializers.ModelSerializer): 
    user = UserSerializer(read_only=True)
    cart_products = CartProductSerializer(many=True)
    class Meta : 
        model = Cart 
        fields = ["id","user","is_open","is_paid","cart_products"]