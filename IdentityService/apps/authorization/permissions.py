"""Permissions helpers for the `authorization` app."""
try:
    from rest_framework.permissions import BasePermission
except Exception:
    BasePermission = object


class HasPermission(BasePermission):
    def __init__(self, permission_name=None):
        self.permission_name = permission_name

    def has_permission(self, request, view):
        user = getattr(request, 'user', None)
        return bool(user and getattr(user, 'is_authenticated', False))
