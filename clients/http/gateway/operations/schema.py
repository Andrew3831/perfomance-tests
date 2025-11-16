from enum import StrEnum
from pydantic import BaseModel, Field, ConfigDict


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    PURCHASE = "PURCHASE"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    CREATED = "CREATED"
    COMPLETED = "COMPLETED"


class MakeTopUpOperationRequestSchema(BaseModel):
    """
    Модель запроса для создания операции пополнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(alias="status")
    amount: float = Field(alias="amount")
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")
    operation_type: OperationType = Field(default=OperationType.TOP_UP, alias="operationType")


class OperationSchema(BaseModel):
    """
    Модель операции, которую возвращает API.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str = Field(alias="id")
    type: OperationType = Field(alias="type")
    status: OperationStatus = Field(alias="status")
    amount: float = Field(alias="amount")
    card_id: str = Field(alias="cardId")
    category: str | None = Field(default=None, alias="category")
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Ответ API на создание операции пополнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    operation: OperationSchema = Field(alias="operation")


