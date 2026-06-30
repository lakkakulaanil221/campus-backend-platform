"""Signals for the `audit` app."""
from django.dispatch import Signal, receiver

audit_created = Signal()


@receiver(audit_created)
def handle_audit_created(sender, **kwargs):
    # placeholder receiver
    return None
