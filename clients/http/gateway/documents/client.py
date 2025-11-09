from typing import TypedDict
from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class DocumentDict(TypedDict):
    """
    Представление документа.
    """
    url: str
    document: str


class GetTariffDocumentResponseDict(TypedDict):
    """
    Ответ на запрос получения тарифного документа.
    """
    tariff: DocumentDict


class GetContractDocumentResponseDict(TypedDict):
    """
    Ответ на запрос получения документа контракта.
    """
    contract: DocumentDict


class DocumentsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с сервисами документов (/api/v1/documents).
    """

    def get_tariff_document_api(self, account_id: str) -> Response:
        """
        Метод получает тарифный документ по идентификатору счета.

        :param account_id: Идентификатор счета.
        :return: Ответ сервера (httpx.Response).
        """
        return self.get(f"/api/v1/documents/tariff-document/{account_id}")

    def get_contract_document_api(self, account_id: str) -> Response:
        """
        Метод получает документ контракта по идентификатору счета.

        :param account_id: Идентификатор счета.
        :return: Ответ сервера (httpx.Response).
        """
        return self.get(f"/api/v1/documents/contract-document/{account_id}")

    # Новый метод для получения тарифного документа
    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseDict:
        """
        Получает тарифный документ по идентификатору счета.

        :param account_id: Идентификатор счета.
        :return: Распарсенный JSON-ответ.
        """
        response = self.get_tariff_document_api(account_id)
        return response.json()

    # Новый метод для получения документа контракта
    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseDict:
        """
        Получает документ контракта по идентификатору счета.

        :param account_id: Идентификатор счета.
        :return: Распарсенный JSON-ответ.
        """
        response = self.get_contract_document_api(account_id)
        return response.json()


def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    """
    Строит и возвращает настроенный DocumentsGatewayHTTPClient.

    :return: Настроенный DocumentsGatewayHTTPClient.
    """
    return DocumentsGatewayHTTPClient(client=build_gateway_http_client())

