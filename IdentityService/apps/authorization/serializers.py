"""Serializers for the `authorization` app."""
try:
    from rest_framework import serializers
except Exception:
    serializers = None


if serializers:
    class PermissionSerializer(serializers.Serializer):
        name = serializers.CharField()
else:
    class PermissionSerializer:
        pass
