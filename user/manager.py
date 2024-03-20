from django.contrib.auth.models import BaseUserManager
class UserManager(BaseUserManager):
    """ 
        manager for User model 
        Args:
           required : email , password 
           optional : first_name , last_name
    """
    def create_user(self,email,password,**kwargs):
        if not email : 
            raise ValueError("email field is required .")
        if not password : 
            raise ValueError("password field is required .")
        user = self.model(email=email,**kwargs)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password,**kwargs):
        kwargs.setdefault("is_active",True)
        kwargs.setdefault("is_staff",True)
        kwargs.setdefault("is_superuser",True)
        if not kwargs.get("is_active") : raise ValueError('superuser must have is_active=True')
        if not kwargs.get("is_staff") : raise ValueError('superuser must have is_staff=True')
        if not kwargs.get("is_superuser") : raise ValueError('superuser must have is_superuser=True')
        return self.create_user(email=email,password=password,**kwargs)