"""Domain validation for catalog evidence envelopes."""

from evidence_catalog.validation import (
    ValidationError, boolean, fields, identifier, integer, text,
)

PROJECT = 'certificate-renewal-planner'


def validate_payload(payload):

    fields(payload, ("id", "earliest", "deadline"))
    identifier(payload["id"], "certificate id")
    integer(payload["earliest"], "earliest day")
    integer(payload["deadline"], "deadline day")


def example_payload():
    return {'id': 'cert-01', 'earliest': 1, 'deadline': 30}
