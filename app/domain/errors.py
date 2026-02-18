from app.domain.enums.business_error_code import BusinessErrorCode

class DomainError(Exception):
    def __init__(self, message: str, code: str):
        super().__init__(message)
        self.message = message
        self.code=code

class NotFoundError(DomainError):
    def __init__(self, business_error_code: BusinessErrorCode):
        super().__init__(business_error_code.message, business_error_code.code)
    """Raised when a requested resource is not found."""

class ServiceError(DomainError):
   def __init__(self, business_error_code: BusinessErrorCode):
        super().__init__(business_error_code.message, business_error_code.code)

class ValidationError(DomainError):
    def __init__(self, business_error_code: BusinessErrorCode):
        super().__init__(business_error_code.message, business_error_code.code)