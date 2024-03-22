from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from product.models import Category,Product,SubCategory
from product.serializers import CategorySerializer,ProductSerializer,SubcategorySerializer
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

# sub categories
class SubcategoryListCreateAPIView(APIView):
    permission_classes = [IsStaffOrReadOnly]
    def get(self,request,category_id):
        try :
            category = Category.objects.get(id=category_id)
        except :
            return Response(data={"detail":"category with this id doesnt exist "},status=status.HTTP_400_BAD_REQUEST)
        return Response(data=SubcategorySerializer(
            category.sub_categories.all(),
            many=True ,
            context = {"request":request}
        ).data)
    def post(self,request,category_id):
        try :
            category = Category.objects.get(id=category_id)
        except :
            return Response(data={"detail":"category with this id doesnt exist "},status=status.HTTP_400_BAD_REQUEST)
        data = request.data.copy()
        data["cateogry"] = category
        serializer = SubcategorySerializer(data=request.data,context={"request":request})
        if serializer.is_valid() :
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class ListSubcategoryAPIView(ListAPIView):
    queryset = SubCategory.objects.all()
    permission_classes = [IsStaffOrReadOnly]
    serializer_class = SubcategorySerializer
class SubCategoryAPIView(APIView):
    permission_classes = [IsStaffOrReadOnly]
    def get_subcategory(self,sub_category_id):
        try :
            self.sub_category = SubCategory.objects.get(id=sub_category_id)
        except :
            self.sub_category = None
            return Response(data={"detail":"sub category with this is doenst exsit"},status=status.HTTP_400_BAD_REQUEST)
    def dispatch(self,request,subcategory_id):
        self.get_subcategory(subcategory_id)
        return super().dispatch(request,subcategory_id)
    def get(self,request,subcategory_id):
        if not self.sub_category :
            return self.get_subcategory(subcategory_id)
        return Response(data=SubcategorySerializer(self.sub_category,context={"request":request}).data)
    def put(self,request,subcategory_id):
        if not self.sub_category :
            return self.get_subcategory(subcategory_id)
        serializer = SubcategorySerializer(
            data=request.data,
            instance=self.sub_category,
            context= {"request":request},
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response (data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,subcategory_id):
        if not self.sub_category :
            return self.get_subcategory(subcategory_id)
        self.sub_category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# product
class ProductAPI : 
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
    permission_classes = [IsStaffOrReadOnly]
class ProductListCreateAPIView(ProductAPI,ListCreateAPIView):
    pass 
class ProductAPIView(ProductAPI,RetrieveUpdateDestroyAPIView):
    pass 