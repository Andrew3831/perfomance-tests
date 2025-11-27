import logging

from httpx import Client
from locust.env import Environment

from clients.http.event_hooks.locust_event_hook import (
    locust_request_event_hook,
    locust_response_event_hook
)
from config import settings


def build_gateway_http_client() -> Client:
    """
    Стандартный HTTP-клиент для http-gateway.
    Все параметры берутся из глобальных настроек.
    """
    return Client(
        timeout=settings.gateway_http_client.timeout,
        base_url=settings.gateway_http_client.client_url
    )


def build_gateway_locust_http_client(environment: Environment) -> Client:
    """
    HTTP-клиент для Locust.
    Настройки загружаются из конфигурации,
    а события отправляются через event_hooks.
    """
    logging.getLogger("httpx").setLevel(logging.WARNING)

    return Client(
        timeout=settings.gateway_http_client.timeout,
        base_url=settings.gateway_http_client.client_url,
        event_hooks={
            "request": [locust_request_event_hook],
            "response": [locust_response_event_hook(environment)]
        }
    )
