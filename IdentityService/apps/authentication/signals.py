"""Signals for the `authentication` app."""
from django.dispatch import Signal, receiver

user_logged_in = Signal()


@receiver(user_logged_in)
def handle_user_logged_in(sender, **kwargs):
    return None
