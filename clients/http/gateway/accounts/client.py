from typing import TypedDict
from httpx import Response, QueryParams

from clients.http.client import HTTPClient


# Базовые типы для полей запросов
class BaseOperationDict(TypedDict):
    """
    Базовая структура данных для общих полей операций.
    """
    account_id: str
    amount: float


class BaseMakeOperationRequestDict(BaseOperationDict):
    """
    Базовая структура данных для создания операций.
    """
    status: str


# Специализированные структуры данных для конкретных операций
class OperationInfoDict(TypedDict):
    """
    Структура данных для получения информации об отдельной операции.
    """
    operation_id: str


class GetOperationReceiptApiDict(TypedDict):
    """
    Структура данных для получения чека по операции.
    """
    operation_id: str


class GetOperationsApiDict(TypedDict):
    """
    Структура данных для получения списка операций по счету.
    """
    account_id: str


class GetOperationsSummaryApiDict(TypedDict):
    """
    Структура данных для получения сводки операций по счету.
    """
    account_id: str


class FeeOperationApiDict(BaseMakeOperationRequestDict):
    """
    Структура данных для создания операции комиссии.
    """
    fee_type: str


class TopUpOperationRequestDict(BaseMakeOperationRequestDict):
    """
    Структура данных для создания операции пополнения.
    """
    top_up_method: str


class CashbackOperationRequestDict(BaseMakeOperationRequestDict):
    """
    Структура данных для создания операции кэшбэка.
    """
    cashback_category: str


class TransferOperationRequestDict(BaseMakeOperationRequestDict):
    """
    Структура данных для создания операции перевода.
    """
    destination_account_id: str


class PurchaseOperationRequestDict(BaseMakeOperationRequestDict):
    """
    Структура данных для создания операции покупки.
    """
    purchase_description: str


class BillPaymentOperationRequestDict(BaseMakeOperationRequestDict):
    """
    Структура данных для создания операции оплаты по счету.
    """
    bill_number: str


class CashWithdrawalOperationRequestDict(BaseMakeOperationRequestDict):
    """
    Структура данных для создания операции снятия наличных.
    """
    withdrawal_location: str


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с сервисом операций (/api/v1/operations) http-gateway.
    """

    # Методы для получения информации
    def get_operation_api(self, info: OperationInfoDict) -> Response:
        """
        Выполняет GET-запрос на получение информации об операции по её ID.

        :param info: Словарь с информацией об операции, включая operation_id.
        :return: Объект httpx.Response с деталями операции.
        """
        operation_id = info["operation_id"]
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, info: GetOperationReceiptApiDict) -> Response:
        """
        Выполняет GET-запрос на получение чека по конкретной операции.

        :param info: Словарь с информацией об операции, включая operation_id.
        :return: Объект httpx.Response с чеком операции.
        """
        operation_id = info["operation_id"]
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, summary: GetOperationsApiDict) -> Response:
        """
        Выполняет GET-запрос на получение списка операций по указанному счету.

        :param summary: Словарь с указанием аккаунта, например {"account_id": "123"}.
        :return: Объект httpx.Response с перечнем операций.
        """
        return self.get("/api/v1/operations", params=QueryParams(**summary))

    def get_operations_summary_api(self, summary: GetOperationsSummaryApiDict) -> Response:
        """
        Выполняет GET-запрос на получение сводки операций по заданному аккаунту.

        :param summary: Словарь с указанием аккаунта, например {"account_id": "123"}.
        :return: Объект httpx.Response с обобщёнными данными по операциям.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**summary))

    # Методы для создания операций
    def make_fee_operation_api(self, request: FeeOperationApiDict) -> Response:
        """
        Выполняет POST-запрос для создания операции комиссии.

        :param request: Словарь с данными о создании комиссии.
        :return: Объект httpx.Response с результатами операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: TopUpOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции пополнения.

        :param request: Словарь с данными о пополнении.
        :return: Объект httpx.Response с результатами операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: CashbackOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции кэшбэка.

        :param request: Словарь с данными о кэшбэке.
        :return: Объект httpx.Response с результатами операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: TransferOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции перевода.

        :param request: Словарь с данными о переводе.
        :return: Объект httpx.Response с результатами операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: PurchaseOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции покупки.

        :param request: Словарь с данными о покупке.
        :return: Объект httpx.Response с результатами операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: BillPaymentOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты по счету.

        :param request: Словарь с данными об оплате по счету.
        :return: Объект httpx.Response с результатами операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: CashWithdrawalOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции снятия наличных.

        :param request: Словарь с данными о снятии наличных.
        :return: Объект httpx.Response с результатами операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)