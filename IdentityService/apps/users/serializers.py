"""Serializers for the `users` app."""
try:
    from rest_framework import serializers
except Exception:
    serializers = None


if serializers:
    class UserSerializer(serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
        username = serializers.CharField()
else:
    class UserSerializer:
        pass
