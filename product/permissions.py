from rest_framework.permissions import BasePermission,SAFE_METHODS
class IsStaffOrReadOnly(BasePermission):
    def has_permission(self,request,view):
        if request.method in SAFE_METHODS :
            return True
        elif request.user.is_authenticated :
            return request.user.is_staff