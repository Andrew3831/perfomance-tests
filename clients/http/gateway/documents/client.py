from httpx import Response
from locust.env import Environment

from clients.http.client import HTTPClient, HTTPClientExtensions
from clients.http.gateway.client import (
    build_gateway_http_client,
    build_gateway_locust_http_client,
)
from clients.http.gateway.documents.schema import (
    GetTariffDocumentResponseSchema,
    GetContractDocumentResponseSchema,
)


class DocumentsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/documents сервиса http-gateway.
    """

    def get_tariff_document_api(self, account_id: str) -> Response:
        return self.get(
            f"/api/v1/documents/tariff-document/{account_id}",
            extensions=HTTPClientExtensions(
                route="/api/v1/documents/tariff-document/{account_id}"
            )
        )

    def get_contract_document_api(self, account_id: str) -> Response:
        return self.get(
            f"/api/v1/documents/contract-document/{account_id}",
            extensions=HTTPClientExtensions(
                route="/api/v1/documents/contract-document/{account_id}"
            )
        )

    # ---------- High-level методы ----------

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseSchema:
        response = self.get_tariff_document_api(account_id)
        return GetTariffDocumentResponseSchema.model_validate_json(response.text)

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseSchema:
        response = self.get_contract_document_api(account_id)
        return GetContractDocumentResponseSchema.model_validate_json(response.text)


def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    return DocumentsGatewayHTTPClient(client=build_gateway_http_client())


def build_documents_gateway_locust_http_client(environment: Environment) -> DocumentsGatewayHTTPClient:
    # ----------------------------------------------------
    # Билдер для LOCUST
    # ----------------------------------------------------
    # Создаёт DocumentsGatewayHTTPClient, адаптированный под нагрузочные тесты:
    #   - автоматически подключается к Locust Environment
    #   - отправляет туда метрики выполнения каждого http-запроса
    #   - используется только в performance/load тестировании
    return DocumentsGatewayHTTPClient(
        client=build_gateway_locust_http_client(environment)
    )
