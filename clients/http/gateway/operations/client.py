from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client

from clients.http.gateway.operations.schema import (
    MakeTopUpOperationRequestSchema,
    MakeTopUpOperationResponseSchema,
)


class OperationsGatewayHTTPClient(HTTPClient):

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestSchema):
        return self.post(
            "/api/v1/operations/make-top-up-operation",
            json=request.model_dump(by_alias=True)
        )

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseSchema:

        request = MakeTopUpOperationRequestSchema(
            status="COMPLETED",
            amount=1500.11,
            operation_type="TOP_UP",
            card_id=card_id,
            account_id=account_id,
        )

        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())

