"""Validators for the `authentication` app."""
from django.core.exceptions import ValidationError


def validate_password_strength(password):
    if not password:
        raise ValidationError('Password cannot be empty')
