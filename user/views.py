from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from user.serializers import RegisterSerializer,UserSerializer
from user.send_email import send_email
from rest_framework_simplejwt.views import TokenObtainPairView
@api_view(["POST"])
def register_user_api_view(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid() : 
        user = serializer.save()
        user.set_password(user.password)
        user.save()
        send_email(user=user)
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(["POST"])
def activate_email_api_view(request):
    email,otp_code = (request.data.get("email"),request.data.get("otp_code"))
    if not email or not otp_code : 
        return Response(data={"detail":"email and otp_code is required"},status=status.HTTP_400_BAD_REQUEST)
    try : 
        user = get_user_model().objects.get(email=email)
    except :
        return Response(data={"detail":"email or otp_code is incorrect."},status=status.HTTP_400_BAD_REQUEST)
    if str(user.otp_code) == otp_code : 
        user.is_active = True 
        user.save()
        refresh_token = RefreshToken.for_user(user)
        return Response(data={
            "user" : UserSerializer(user).data,
            "refresh_token" : str(refresh_token),
            "access_token" : str(refresh_token.access_token),
        })
    return Response(data={"detail":"email or otp_code is incorrect."},status=status.HTTP_400_BAD_REQUEST)
@api_view(["POST"])
def login_user_api_view(request):
    email,password = (request.data.get("email"),request.data.get("password"))
    if not email or not password : 
        return Response(data={"detail":"email and password is request"},status=status.HTTP_400_BAD_REQUEST)
    try : 
        user = get_user_model().objects.get(email=email)
    except :
        return Response(data={"detail":"email or password is incorrect."},status=status.HTTP_400_BAD_REQUEST)
    if user.check_password(password) :
        refresh_token = RefreshToken.for_user(user)
        return Response(data={
            "user" : UserSerializer(user).data,
            "refresh_token" : str(refresh_token),
            "access_token" : str(refresh_token.access_token),
        })
    return Response(data={"detail":"email or password is incorrect."},status=status.HTTP_400_BAD_REQUEST)