"""Signals for the `users` app."""
from django.dispatch import Signal, receiver

user_created = Signal()


@receiver(user_created)
def handle_user_created(sender, **kwargs):
    return None
