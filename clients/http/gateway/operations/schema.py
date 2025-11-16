from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field, HttpUrl, ConfigDict

from tools.fakers import fake


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationSchema(BaseModel):
    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: datetime = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationReceiptSchema(BaseModel):
    url: HttpUrl
    document: str


class OperationsSummarySchema(BaseModel):
    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


class GetOperationResponseSchema(BaseModel):
    operation: OperationSchema


class GetOperationsQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")


class GetOperationsResponseSchema(BaseModel):
    operations: list[OperationSchema]


class GetOperationsSummaryQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")


class GetOperationsSummaryResponseSchema(BaseModel):
    summary: OperationsSummarySchema


class GetOperationReceiptResponseSchema(BaseModel):
    receipt: OperationReceiptSchema


# -----------------------------
# BASE REQUEST MODEL
# -----------------------------

class MakeOperationRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=lambda: fake.amount())

    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    pass


class MakeFeeOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    pass


class MakeTopUpOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    pass


class MakeCashbackOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    pass


class MakeTransferOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    category: str = Field(default_factory=fake.category)


class MakePurchaseOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    pass


class MakeBillPaymentOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    pass


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    operation: OperationSchema

