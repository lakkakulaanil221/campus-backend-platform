"""Signals for the `authorization` app."""
from django.dispatch import Signal, receiver

permission_granted = Signal()


@receiver(permission_granted)
def _on_permission_granted(sender, **kwargs):
    return None
