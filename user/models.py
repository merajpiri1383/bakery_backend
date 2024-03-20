from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django_jalali.db.models import jDateTimeField
from user.manager import UserManager
from random import randint
class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(db_index=True,unique=True)
    first_name = models.CharField(blank=True,null=True,max_length=150)
    last_name = models.CharField(blank=True,null=True,max_length=150)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    otp_code = models.PositiveIntegerField(null=True,blank=True)
    joind = jDateTimeField(auto_now_add=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()
    def save(self,**kwargs):
        self.otp_code = randint(100000,999999)
        return super().save(**kwargs)
    @property 
    def username(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self): 
        return f"User : {self.email}"