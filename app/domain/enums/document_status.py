from enum import Enum

class DocumentStatus(Enum):
    DRAFT = "draft" 
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"