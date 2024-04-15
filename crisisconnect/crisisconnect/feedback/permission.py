from rest_framework import permissions
from rest_framework.request import Request


class IsCollector(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        if request.user.is_authenticated and request.user.position == "C":
            return True
