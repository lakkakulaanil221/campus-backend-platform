"""Validators for the `authorization` app."""
from django.core.exceptions import ValidationError


def validate_permission_name(name):
    if not name:
        raise ValidationError('Permission name required')
