
class DomainError(Exception):
    def __init__(self, message: str, code: str):
        super().__init__(message)
        self.message = message
        self.code=code

class NotFoundError(DomainError):
    """Raised when a requested resource is not found."""

class ServiceError(DomainError):
   """Raised when an external service call fails."""

class ValidationError(DomainError):
    """Raised when input validation fails."""


