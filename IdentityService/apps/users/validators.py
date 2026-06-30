"""Validators for the `users` app."""
from django.core.exceptions import ValidationError


def validate_username(value):
    if not value or not str(value).strip():
        raise ValidationError('Username cannot be blank.')
