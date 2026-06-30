"""Permissions for the `users` app."""
try:
    from rest_framework.permissions import BasePermission
except Exception:
    BasePermission = object


class IsUserOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return bool(getattr(getattr(request, 'user', None), 'is_authenticated', False))
        return getattr(getattr(request, 'user', None), 'is_staff', False)
