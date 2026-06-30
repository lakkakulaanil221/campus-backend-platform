"""Serializers for the `audit` app (template placeholders)."""
try:
    from rest_framework import serializers
except Exception:
    serializers = None


if serializers:
    class AuditSerializer(serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
        created_at = serializers.DateTimeField(required=False)
else:
    class AuditSerializer:
        """Fallback placeholder when DRF is not available."""
        pass
