from typing import TypedDict
from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client

from typing import TypedDict, List

class OperationDict(TypedDict):
    """
    Операция транзакции.
    """
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str

class OperationReceiptDict(TypedDict):
    """
    Чек по операции.
    """
    url: str
    document: str

class OperationsSummaryDict(TypedDict):
    """
    Резюме операций.
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float
class GetOperationRequestDict(TypedDict):
    """
    Параметры запроса для получения конкретной операции.
    """
    operationId: str

class GetOperationResponseDict(TypedDict):
    """
    Структура ответа на запрос получения одной операции.
    """
    operation: OperationDict

class GetOperationReceiptRequestDict(TypedDict):
    """
    Параметры запроса для получения чека операции.
    """
    operationId: str

class GetOperationReceiptResponseDict(TypedDict):
    """
    Структура ответа на запрос получения чека операции.
    """
    receipt: OperationReceiptDict

class GetOperationsQueryDict(TypedDict):
    """
    Параметры запроса для получения списка операций.
    """
    accountId: str

class GetOperationsResponseDict(TypedDict):
    """
    Структура ответа на запрос получения списка операций.
    """
    operations: List[OperationDict]

class GetOperationsSummaryQueryDict(TypedDict):
    """
    Параметры запроса для получения резюме операций.
    """
    accountId: str

class GetOperationsSummaryResponseDict(TypedDict):
    """
    Структура ответа на запрос получения резюме операций.
    """
    summary: OperationsSummaryDict

class MakeFeeOperationRequestDict(TypedDict):
    """
    Параметры запроса для комиссии.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeFeeOperationResponseDict(TypedDict):
    """
    Структура ответа на запрос внесения комиссии.
    """
    operation: OperationDict

class MakeTopUpOperationRequestDict(TypedDict):
    """
    Параметры запроса для пополнения счета.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeTopUpOperationResponseDict(TypedDict):
    """
    Структура ответа на запрос пополнения счета.
    """
    operation: OperationDict

class MakeCashbackOperationRequestDict(TypedDict):
    """
    Параметры запроса для возврата кэшбека.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeCashbackOperationResponseDict(TypedDict):
    """
    Структура ответа на запрос начисления кэшбека.
    """
    operation: OperationDict

class MakeTransferOperationRequestDict(TypedDict):
    """
    Параметры запроса для перевода денег.
    """
    status: str
    amount: float
    sourceCardId: str
    destinationCardId: str
    accountId: str

class MakeTransferOperationResponseDict(TypedDict):
    """
    Структура ответа на запрос перевода денег.
    """
    operation: OperationDict

class MakePurchaseOperationRequestDict(TypedDict):
    """
    Параметры запроса для покупки товаров.
    """
    status: str
    amount: float
    cardId: str
    merchantCategoryCode: str
    accountId: str

class MakePurchaseOperationResponseDict(TypedDict):
    """
    Структура ответа на запрос оплаты покупок.
    """
    operation: OperationDict

class MakeBillPaymentOperationRequestDict(TypedDict):
    """
    Параметры запроса для платежа по счету.
    """
    status: str
    amount: float
    billId: str
    accountId: str

class MakeBillPaymentOperationResponseDict(TypedDict):
    """
    Структура ответа на запрос оплаты счета.
    """
    operation: OperationDict

class MakeCashWithdrawalOperationRequestDict(TypedDict):
    """
    Параметры запроса для снятия наличных.
    """
    status: str
    amount: float
    atmLocation: str
    cardId: str
    accountId: str

class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """
    Структура ответа на запрос снятия наличных.
    """
    operation: OperationDict


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с сервисом операций (/api/v1/operations).
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение конкретной операции.

        :param operation_id: Уникальный идентификатор операции.
        :return: Ответ сервера (httpx.Response).
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по конкретной операции.

        :param operation_id: Уникальный идентификатор операции.
        :return: Ответ сервера (httpx.Response).
        """
        return self.get(f"/api/v1/operations/receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получение списка операций по счету.

        :param query: Словарь с параметром accountId.
        :return: Ответ сервера (httpx.Response).
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Получение резюме операций по счету.

        :param query: Словарь с параметром accountId.
        :return: Ответ сервера (httpx.Response).
        """
        return self.get("/api/v1/operations/summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Выполнение операции комиссии.

        :param request: Словарь с данными операции.
        :return: Ответ сервера (httpx.Response).
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Выполнение операции пополнения счета.

        :param request: Словарь с данными операции.
        :return: Ответ сервера (httpx.Response).
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Выполнение операции начисления кэшбека.

        :param request: Словарь с данными операции.
        :return: Ответ сервера (httpx.Response).
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Выполнение операции перевода денег.

        :param request: Словарь с данными операции.
        :return: Ответ сервера (httpx.Response).
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполнение операции покупки товара.

        :param request: Словарь с данными операции.
        :return: Ответ сервера (httpx.Response).
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Выполнение операции оплаты счета.

        :param request: Словарь с данными операции.
        :return: Ответ сервера (httpx.Response).
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Выполнение операции снятия наличных.

        :param request: Словарь с данными операции.
        :return: Ответ сервера (httpx.Response).
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    # Высокоуровневые методы

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        """
        Получение конкретной операции.

        :param operation_id: Уникальный идентификатор операции.
        :return: Отпарсированный JSON-ответ.
        """
        response = self.get_operation_api(operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        """
        Получение чека по конкретной операции.

        :param operation_id: Уникальный идентификатор операции.
        :return: Отпарсированный JSON-ответ.
        """
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        """
        Получение списка операций по данному счету.

        :param account_id: Идентификатор счета.
        :return: Отпарсированный JSON-ответ.
        """
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        """
        Получение резюме операций по данному счету.

        :param account_id: Идентификатор счета.
        :return: Отпарсированный JSON-ответ.
        """
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        """
        Выполнить операцию комиссии.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Отпарсированный JSON-ответ.
        """
        request = MakeFeeOperationRequestDict(status="COMPLETED", amount=55.77, cardId=card_id, accountId=account_id)
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        """
        Выполнить операцию пополнения счета.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Отпарсированный JSON-ответ.
        """
        request = MakeTopUpOperationRequestDict(status="COMPLETED", amount=1500.11, cardId=card_id, accountId=account_id)
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        """
        Выполнить операцию начисления кэшбека.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Отпарсированный JSON-ответ.
        """
        request = MakeCashbackOperationRequestDict(status="COMPLETED", amount=50.0, cardId=card_id, accountId=account_id)
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, source_card_id: str, destination_card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        """
        Выполнить операцию перевода денежных средств.

        :param source_card_id: Идентификатор исходящей карты.
        :param destination_card_id: Идентификатор принимающей карты.
        :param account_id: Идентификатор счета.
        :return: Отпарсированный JSON-ответ.
        """
        request = MakeTransferOperationRequestDict(status="COMPLETED", amount=1000.0, sourceCardId=source_card_id, destinationCardId=destination_card_id, accountId=account_id)
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str, merchant_category_code: str) -> MakePurchaseOperationResponseDict:
        """
        Выполнить операцию покупки товара.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :param merchant_category_code: Код категории продавца.
        :return: Отпарсированный JSON-ответ.
        """
        request = MakePurchaseOperationRequestDict(status="COMPLETED", amount=500.0, cardId=card_id, merchantCategoryCode=merchant_category_code, accountId=account_id)
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, bill_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        """
        Выполнить оплату счета.

        :param bill_id: Идентификатор счета.
        :param account_id: Идентификатор счета плательщика.
        :return: Отпарсированный JSON-ответ.
        """
        request = MakeBillPaymentOperationRequestDict(status="COMPLETED", amount=100.0, billId=bill_id, accountId=account_id)
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str, atm_location: str) -> MakeCashWithdrawalOperationResponseDict:
        """
        Выполнить снятие наличных.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :param atm_location: Местоположение банкомата.
        :return: Отпарсированный JSON-ответ.
        """
        request = MakeCashWithdrawalOperationRequestDict(status="COMPLETED", amount=500.0, atmLocation=atm_location, cardId=card_id, accountId=account_id)
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция строит экземпляр OperationsGatewayHTTPClient с готовым HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())