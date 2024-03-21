from rest_framework.generics import ListAPIView
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from cart.serializers import CartSerializer,CartProductSerializer
from cart.models import Cart,CartProduct
from cart.permissions import IsStaffPermission
from product.models import Product
from rest_framework.permissions import IsAuthenticated
class CartListAPIView(ListAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    permission_classes = [IsStaffPermission]
class CartAPIView(APIView):
    """  get | change | delete cart
    """
    def get(self,request,cart_id): 
        try :
            cart = Cart.objects.get(id=cart_id)
            return Response(data=CartSerializer(cart).data)
        except :
            return Response(data={"detail":"cart with this id doenst exist"},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,cart_id):
        try :
            Cart.objects.get(id=cart_id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except :
            return Response(data={"detail":"cart with this id doenst exist"},status=status.HTTP_400_BAD_REQUEST)
class CartProductAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def set_cart_and_product(self,request,product_id):
        self.cart,created = Cart.objects.get_or_create(user=request.user,is_open=True)
        try :
            self.product = Product.objects.get(id=product_id)
        except :
            return Response(data={"detail":"product with this id doesnt exist"},status=status.HTTP_400_BAD_REQUEST)
        self.cart_product,create = CartProduct.objects.get_or_create(cart=self.cart, product=self.product)
    def post(self,request,product_id):
        if self.set_cart_and_product(request,product_id) :
            return self.set_cart_and_product(request,product_id)
        self.cart_product.count = self.cart_product.count + 1
        self.cart_product.save()
        return Response(data=CartSerializer(self.cart).data)
    def delete(self,request,product_id):
        if self.set_cart_and_product(request, product_id) :
            return self.set_cart_and_product(request, product_id)
        if self.cart_product.count == 1 :
            self.cart_product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif self.cart_product.count == 0 :
            return Response(data={"detail":"cart_product doenst exist "},status=status.HTTP_400_BAD_REQUEST)
        else:
            self.cart_product.count = self.cart_product.count - 1
            self.cart_product.save()
            return Response(data=CartSerializer(self.cart).data)