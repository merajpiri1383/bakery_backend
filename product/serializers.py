from rest_framework import serializers 
from product.models import Category,Product
from django_jalali.serializers.serializerfield import JDateTimeField
class ProductMiniSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Product 
        fields = ["id","name","image","created","updated"]
    def to_representation(self,instance):
            constext = super().to_representation(instance)
            constext["created"] = instance.created.strftime("%Y-%m-%d")
            constext["updated"] = instance.updated.strftime("%Y-%m-%d")
            return constext
class CategorySerializer(serializers.ModelSerializer):
    products = ProductMiniSerializer(many=True,read_only=True)
    class Meta : 
        model = Category 
        fields = ["id","name","image","products"]
class ProductSerializer(ProductMiniSerializer):
    class Meta : 
        model = Product 
        fields = "__all__"