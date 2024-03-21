from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from product.models import Category,Product
from product.serializers import CategorySerializer,ProductSerializer
from product.permissions import  IsStaffOrReadOnly
# category 
class CategoryAPI :
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]
class CategoryListCreateAPIView(CategoryAPI,ListCreateAPIView):
    pass
class CategoryAPIView(CategoryAPI,RetrieveUpdateDestroyAPIView):
    pass
# product
class ProductAPI : 
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
    permission_classes = [IsStaffOrReadOnly]
class ProductListCreateAPIView(ProductAPI,ListCreateAPIView):
    pass 
class ProductAPIView(ProductAPI,RetrieveUpdateDestroyAPIView):
    pass 