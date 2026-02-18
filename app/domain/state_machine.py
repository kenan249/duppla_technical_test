from app.domain.enums.document_status import DocumentStatus

ALLOWED_TRANSITIONS: dict[DocumentStatus, set[DocumentStatus]] = {
    DocumentStatus.DRAFT: {DocumentStatus.PENDING},
    DocumentStatus.PENDING: {DocumentStatus.APPROVED, DocumentStatus.REJECTED},
    DocumentStatus.APPROVED: set(),
    DocumentStatus.REJECTED: set(),
}


def can_transition(from_status: DocumentStatus, to_status: DocumentStatus) -> bool:
    """Check if transition from one status to another is allowed."""
    allowed = ALLOWED_TRANSITIONS.get(from_status, set())
    return to_status in allowed