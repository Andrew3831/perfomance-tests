from pydantic import BaseModel, Field
from typing import Optional


class DocumentSchema(BaseModel):
    """
    Модель простого документа.
    """
    url: str
    document: str


class GetTariffDocumentResponseSchema(BaseModel):
    """
    Модель ответа на запрос получения тарифного документа.
    """
    tariff: DocumentSchema


class GetContractDocumentResponseSchema(BaseModel):
    """
    Модель ответа на запрос получения контрактного документа.
    """
    contract: DocumentSchema