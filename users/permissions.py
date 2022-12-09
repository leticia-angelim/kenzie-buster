from rest_framework import permissions
from .models import User


class IsEmployeeOrProfileOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, user: User) -> bool:
        if request.user.is_authenticated and request.user.is_employee:
            return True

        return user == request.user
