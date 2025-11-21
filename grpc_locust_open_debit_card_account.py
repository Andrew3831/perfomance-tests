from locust import User, between, task

from clients.grpc.gateway.users.client import (
    UsersGatewayGRPCClient,
    build_users_gateway_locust_grpc_client,
)
from clients.grpc.gateway.accounts.client import (
    AccountsGatewayGRPCClient,
    build_accounts_gateway_locust_grpc_client,
)

from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse


class OpenDebitCardAccountScenarioUser(User):
    # Обязательный атрибут для Locust
    host = "localhost"
    # Задержка между задачами
    wait_time = between(1, 3)

    # Типы клиентов
    users_gateway_client: UsersGatewayGRPCClient
    accounts_gateway_client: AccountsGatewayGRPCClient

    # Ответ на создание пользователя
    create_user_response: CreateUserResponse

    def on_start(self) -> None:
        """
        Выполняется при запуске каждого виртуального пользователя.
        Инициализируем gRPC API клиентов и создаём нового пользователя.
        """
        # Инициализация gRPC-клиента Users Gateway
        self.users_gateway_client = build_users_gateway_locust_grpc_client(self.environment)

        # Инициализация gRPC-клиента Accounts Gateway
        self.accounts_gateway_client = build_accounts_gateway_locust_grpc_client(self.environment)

        # Создаём пользователя
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_debit_card_account(self):
        """
        Основная нагрузочная задача — открыть дебетовый счёт
        для ранее созданного пользователя.
        """
        self.accounts_gateway_client.open_debit_card_account(
            self.create_user_response.user.id
        )
