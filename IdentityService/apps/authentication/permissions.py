"""Permissions for the `authentication` app."""
try:
    from rest_framework.permissions import BasePermission
except Exception:
    BasePermission = object


class IsAuthenticatedOrCreate(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return getattr(getattr(request, 'user', None), 'is_authenticated', False)
