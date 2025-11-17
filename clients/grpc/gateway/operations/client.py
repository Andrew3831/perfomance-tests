from grpc import Channel

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from tools.fakers import fake

from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import (
    OperationsGatewayServiceStub,
)

from contracts.services.gateway.operations.rpc_get_operation_pb2 import (
    GetOperationRequest,
    GetOperationResponse,
)

from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import (
    GetOperationReceiptRequest,
    GetOperationReceiptResponse,
)

from contracts.services.gateway.operations.rpc_get_operations_pb2 import (
    GetOperationsRequest,
    GetOperationsResponse,
)

from contracts.services.gateway.operations.rpc_get_operations_summary_pb2 import (
    GetOperationsSummaryRequest,
    GetOperationsSummaryResponse,
)

from contracts.services.gateway.operations.rpc_make_fee_operation_pb2 import (
    MakeFeeOperationRequest,
    MakeFeeOperationResponse,
)

from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationRequest,
    MakeTopUpOperationResponse,
)

from contracts.services.gateway.operations.rpc_make_cashback_operation_pb2 import (
    MakeCashbackOperationRequest,
    MakeCashbackOperationResponse,
)

from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import (
    MakeTransferOperationRequest,
    MakeTransferOperationResponse,
)

from contracts.services.gateway.operations.rpc_make_purchase_operation_pb2 import (
    MakePurchaseOperationRequest,
    MakePurchaseOperationResponse,
)

from contracts.services.gateway.operations.rpc_make_bill_payment_operation_pb2 import (
    MakeBillPaymentOperationRequest,
    MakeBillPaymentOperationResponse,
)

from contracts.services.gateway.operations.rpc_make_cash_withdrawal_operation_pb2 import (
    MakeCashWithdrawalOperationRequest,
    MakeCashWithdrawalOperationResponse,
)

from contracts.services.operations.operation_pb2 import OperationStatus, OperationType



class OperationsGatewayGRPCClient(GRPCClient):
    """
    gRPC-клиент для взаимодействия с OperationsGatewayService.

    Содержит:
    • низкоуровневые методы (*_api) — прямые gRPC-вызовы
    • высокоуровневые обёртки — удобный интерфейс для прикладной логики
    """

    def __init__(self, channel: Channel):
        """
        Инициализация клиента OperationsGatewayService.

        :param channel: gRPC-канал.
        """
        super().__init__(channel)
        self.stub = OperationsGatewayServiceStub(channel)

    #
    # НИЗКОУРОВНЕВЫЕ API-МЕТОДЫ
    #

    def get_operation_api(self, request: GetOperationRequest) -> GetOperationResponse:
        """Вызов RPC GetOperation."""
        return self.stub.GetOperation(request)

    def get_operation_receipt_api(
        self, request: GetOperationReceiptRequest
    ) -> GetOperationReceiptResponse:
        """Вызов RPC GetOperationReceipt."""
        return self.stub.GetOperationReceipt(request)

    def get_operations_api(self, request: GetOperationsRequest) -> GetOperationsResponse:
        """Вызов RPC GetOperations."""
        return self.stub.GetOperations(request)

    def get_operations_summary_api(
        self, request: GetOperationsSummaryRequest
    ) -> GetOperationsSummaryResponse:
        """Вызов RPC GetOperationsSummary."""
        return self.stub.GetOperationsSummary(request)

    def make_fee_operation_api(
        self, request: MakeFeeOperationRequest
    ) -> MakeFeeOperationResponse:
        """Вызов RPC MakeFeeOperation."""
        return self.stub.MakeFeeOperation(request)

    def make_top_up_operation_api(
        self, request: MakeTopUpOperationRequest
    ) -> MakeTopUpOperationResponse:
        """Вызов RPC MakeTopUpOperation."""
        return self.stub.MakeTopUpOperation(request)

    def make_cashback_operation_api(
        self, request: MakeCashbackOperationRequest
    ) -> MakeCashbackOperationResponse:
        """Вызов RPC MakeCashbackOperation."""
        return self.stub.MakeCashbackOperation(request)

    def make_transfer_operation_api(
        self, request: MakeTransferOperationRequest
    ) -> MakeTransferOperationResponse:
        """Вызов RPC MakeTransferOperation."""
        return self.stub.MakeTransferOperation(request)

    def make_purchase_operation_api(
        self, request: MakePurchaseOperationRequest
    ) -> MakePurchaseOperationResponse:
        """Вызов RPC MakePurchaseOperation."""
        return self.stub.MakePurchaseOperation(request)

    def make_bill_payment_operation_api(
        self, request: MakeBillPaymentOperationRequest
    ) -> MakeBillPaymentOperationResponse:
        """Вызов RPC MakeBillPaymentOperation."""
        return self.stub.MakeBillPaymentOperation(request)

    def make_cash_withdrawal_operation_api(
        self, request: MakeCashWithdrawalOperationRequest
    ) -> MakeCashWithdrawalOperationResponse:
        """Вызов RPC MakeCashWithdrawalOperation."""
        return self.stub.MakeCashWithdrawalOperation(request)

    #
    # ВЫСОКОУРОВНЕВЫЕ ОБЁРТКИ
    #

    def get_operation(self, operation_id: str) -> GetOperationResponse:
        """Обёртка над GetOperation."""
        req = GetOperationRequest(operation_id=operation_id)
        return self.get_operation_api(req)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponse:
        """Обёртка над GetOperationReceipt."""
        req = GetOperationReceiptRequest(operation_id=operation_id)
        return self.get_operation_receipt_api(req)

    def get_operations(self, account_id: str) -> GetOperationsResponse:
        """Обёртка над GetOperations."""
        req = GetOperationsRequest(account_id=account_id)
        return self.get_operations_api(req)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponse:
        """Обёртка над GetOperationsSummary."""
        req = GetOperationsSummaryRequest(account_id=account_id)
        return self.get_operations_summary_api(req)

    #
    #        ОБЁРТКИ ДЛЯ СОЗДАНИЯ ОПЕРАЦИЙ
    #

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponse:
        """Создаёт операцию комиссии."""
        req = MakeFeeOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus),
        )
        return self.make_fee_operation_api(req)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponse:
        """Создаёт операцию пополнения."""
        req = MakeTopUpOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus),
        )
        return self.make_top_up_operation_api(req)

    def make_cashback_operation(
        self, card_id: str, account_id: str
    ) -> MakeCashbackOperationResponse:
        """Создаёт операцию кэшбэка."""
        req = MakeCashbackOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus),
        )
        return self.make_cashback_operation_api(req)

    def make_transfer_operation(
        self, card_id: str, account_id: str
    ) -> MakeTransferOperationResponse:
        """Создаёт операцию перевода."""
        req = MakeTransferOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus),
        )
        return self.make_transfer_operation_api(req)

    def make_purchase_operation(
        self, card_id: str, account_id: str
    ) -> MakePurchaseOperationResponse:
        """Создаёт операцию покупки."""
        req = MakePurchaseOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            category=fake.category(),
            status=fake.proto_enum(OperationStatus),
        )
        return self.make_purchase_operation_api(req)

    def make_bill_payment_operation(
        self, card_id: str, account_id: str
    ) -> MakeBillPaymentOperationResponse:
        """Создаёт операцию оплаты по счёту."""
        req = MakeBillPaymentOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            category=fake.category(),
            status=fake.proto_enum(OperationStatus),
        )
        return self.make_bill_payment_operation_api(req)

    def make_cash_withdrawal_operation(
        self, card_id: str, account_id: str
    ) -> MakeCashWithdrawalOperationResponse:
        """Создаёт операцию снятия наличных."""
        req = MakeCashWithdrawalOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus),
        )
        return self.make_cash_withdrawal_operation_api(req)


def build_operations_gateway_grpc_client() -> OperationsGatewayGRPCClient:
    """
    Фабрика для создания клиента OperationsGatewayService.

    :return: Инициализированный клиент.
    """
    return OperationsGatewayGRPCClient(channel=build_gateway_grpc_client())
