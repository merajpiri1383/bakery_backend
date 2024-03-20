from rest_framework import serializers 
from django.contrib.auth import get_user_model 
import re 
regex_password = re.compile(r"(?=.*[0-9])(?=.*[a-z]){8,16}")
class UserSerializer(serializers.ModelSerializer):
    class Meta : 
        model = get_user_model()
        exclude = ["password","joind"]
    def to_representation(self, instance):
        context = super().to_representation(instance)
        context["joiend_time"] = str(instance.joind.strftime("%H:%M-%S"))
        context["joiend_date"] = str(instance.joind.strftime("%Y-%m-%d"))
        return context
class RegisterSerializer(serializers.ModelSerializer):
    class Meta : 
        model = get_user_model()
        fields = ["email","first_name","last_name","password"]
    def validate(self,data):
        password = data.get("password")
        if not regex_password.findall(password):
            raise serializers.ValidationError("password must contain of 8 numbers and letters .")
        return data