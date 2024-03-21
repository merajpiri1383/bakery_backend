from rest_framework.permissions import BasePermission
class IsStaffPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated :
            return request.user.is_staff