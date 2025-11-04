from typing import TypedDict
from httpx import Response, QueryParams

from clients.http.client import HTTPClient


class OperationInfoDict(TypedDict):
    """
    Структура данных для получения информации об отдельной операции.
    """
    operation_id: str

class GetOperationReceiptApiDict(TypedDict):
    """
    Структура данных для получение чека по операции по operation_id.
    """
    account_id: str

class GetOperationsApiDict(TypedDict):
    """
    Структура данных для получения списка операций для определенного счета
    """
    account_id: str

class GetOperationsSummaryApiDict(TypedDict):
    """
    Структура данных для получения статистики по операциям для определенного счета.
    """
    account_id: str

class FeeOperationApiDict(TypedDict):
    """
    Структура данных для cоздания операции комиссии.
    """
    account_id: str

class TopUpOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции пополнения.
    """
    account_id: str

class CashbackOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции кэшбэка.
    """
    account_id: str

class TransferOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции перевода.
    """
    account_id: str

class PurchaseOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции покупки.
    """
    account_id: str

class BillPaymentOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции оплаты по счету.
    """
    account_id: str

class CashWithdrawalOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции снятия наличных.
    """
    account_id: str

class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с сервисом операций (/api/v1/operations) http-gateway.
    """

    # Методы для получения информации
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