"""Permissions for the `audit` app."""
try:
    from rest_framework.permissions import BasePermission
except Exception:
    BasePermission = object


class IsAuditAdmin(BasePermission):
    """Allow read to anyone, write only to staff users."""
    def has_permission(self, request, view):
        if not hasattr(request, 'method'):
            return False
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        return getattr(getattr(request, 'user', None), 'is_staff', False)
