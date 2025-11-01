from typing import TypedDict
from httpx import Response
from clients.http.client import HTTPClient


class IssueVirtualCardRequestDict(TypedDict):
    """
    Структура данных для выпуска виртуальной банковской карты.
    """
    accountId: int
    cardProductId: int
    pinCode: str
    currency: str
    initialBalance: float
    expiryDate: str
    status: str
    ownerFullName: str
    customCardNumber: str | None
    isMainAccount: bool
    additionalData: dict[str, object]


class IssuePhysicalCardRequestDict(TypedDict):
    """
    Структура данных для выпуска физической банковской карты.
    """
    accountId: int
    cardProductId: int
    pinCode: str
    currency: str
    initialBalance: float
    expiryDate: str
    status: str
    ownerFullName: str
    deliveryAddress: str
    courierServiceId: int
    shipmentMethod: str
    trackingNumber: str | None
    additionalData: dict[str, object]


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с API карточных операций сервиса http-gateway.
    """

    def issue_virtual_card_api(self, request: IssueVirtualCardRequestDict) -> Response:
        """
        Выполняет POST-запрос для выпуска виртуальной банковской карты.

        :param request: Данные для выпуска виртуальной карты.
        :type request: IssueVirtualCardRequestDict
        :return: Ответ сервера (объект httpx.Response).
        :rtype: Response
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: IssuePhysicalCardRequestDict) -> Response:
        """
        Выполняет POST-запрос для выпуска физической банковской карты.

        :param request: Данные для выпуска физической карты.
        :type request: IssuePhysicalCardRequestDict
        :return: Ответ сервера (объект httpx.Response).
        :rtype: Response
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)