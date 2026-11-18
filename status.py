ALLOWED_STATUSES = {
    "DISCOVERED", "SHORTLISTED", "APPLYING", "ATS_PENDING",
    "SUBMITTED_VERIFIED", "ALREADY_APPLIED", "REJECTED",
    "EXPIRED", "BLOCKED", "NEEDS_REVIEW"
}

# Only this explicit evidence gate permits verified submission.
def can_mark_submitted_verified(evidence: dict) -> bool:
    required = ("confirmation_text", "confirmation_url", "application_id")
    return any(str(evidence.get(key, "")).strip() for key in required)

def validate_transition(old_status: str, new_status: str, evidence: dict | None = None) -> None:
    if new_status not in ALLOWED_STATUSES:
        raise ValueError(f"Unknown status: {new_status}")
    if new_status == "SUBMITTED_VERIFIED":
        if not evidence or not can_mark_submitted_verified(evidence):
            raise ValueError("SUBMITTED_VERIFIED requires confirmation evidence.")
