"""Validators for the `audit` app."""
from django.core.exceptions import ValidationError


def validate_not_empty(value):
    if value in (None, ''):
        raise ValidationError('This value may not be empty.')
