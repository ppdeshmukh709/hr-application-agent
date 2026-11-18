import pytest
from src.status import validate_transition

def test_verified_requires_evidence():
    with pytest.raises(ValueError):
        validate_transition("APPLYING", "SUBMITTED_VERIFIED", {})

def test_verified_accepts_confirmation_text():
    validate_transition("APPLYING", "SUBMITTED_VERIFIED",
                        {"confirmation_text": "Application submitted"})
