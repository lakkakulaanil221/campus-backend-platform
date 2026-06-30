"""Serializers for the `authentication` app."""
try:
    from rest_framework import serializers
except Exception:
    serializers = None


if serializers:
    class LoginSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField(write_only=True)
else:
    class LoginSerializer:
        pass
