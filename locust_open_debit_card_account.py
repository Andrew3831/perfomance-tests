from locust import User, between, task

from clients.http.gateway.users.client import (
    UsersGatewayHTTPClient,
    build_users_gateway_locust_http_client,
)
from clients.http.gateway.accounts.client import (
    AccountsGatewayHTTPClient,
    build_accounts_gateway_locust_http_client,
)
from clients.http.gateway.users.schema import CreateUserResponseSchema


class OpenDebitCardAccountScenarioUser(User):
    """
    Нагрузочный сценарий:
    1. Создать пользователя
    2. Открыть дебетовый счёт для созданного пользователя

    Теперь сценарий использует кастомные HTTP API-клиенты.
    """

    # Обязательный атрибут для кастомных Users
    host = "localhost"

    wait_time = between(1, 3)

    # API-клиенты
    users_gateway_client: UsersGatewayHTTPClient
    accounts_gateway_client: AccountsGatewayHTTPClient

    # Ответ после создания пользователя
    create_user_response: CreateUserResponseSchema

    def on_start(self) -> None:
        """
        Метод вызывается при старте каждого виртуального пользователя.
        Здесь мы создаём API-клиенты и нового пользователя.
        """

        # --- 1. Создаём API-клиенты через билдеры для Locust ---
        self.users_gateway_client = build_users_gateway_locust_http_client(self.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_http_client(self.environment)

        # --- 2. Создаём пользователя ---
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_debit_card_account(self):
        """
        Основная нагрузочная задача:
        открытие дебетового счёта для созданного пользователя.
        """

        user_id = self.create_user_response.user.id

        self.accounts_gateway_client.open_debit_card_account(user_id)
