from enum import Enum

class DocumentType(Enum):
    INVOICE = "invoice"
    RECEIPT = "receipt"
    VOUCHER = "voucher"