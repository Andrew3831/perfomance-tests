from locust import task

from clients.grpc.gateway.locust import GatewayGRPCSequentialTaskSet

from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import OpenDebitCardAccountResponse
from contracts.services.gateway.cards.rpc_issue_physical_card_pb2 import IssuePhysicalCardResponse

from tools.locust.user import LocustBaseUser


class IssuePhysicalCardSequentialTaskSet(GatewayGRPCSequentialTaskSet):
    # Здесь будем хранить результаты каждого шага
    create_user_response: CreateUserResponse | None = None
    open_debit_card_account_response: OpenDebitCardAccountResponse | None = None
    issue_physical_card_response: IssuePhysicalCardResponse | None = None

    @task
    def create_user(self):
        # Создаём нового пользователя
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_debit_card_account(self):
        # Счёт можно открыть только после создания пользователя
        if not self.create_user_response:
            return

        self.open_debit_card_account_response = (
            self.accounts_gateway_client.open_debit_card_account(
                user_id=self.create_user_response.user.id
            )
        )

    @task
    def issue_physical_card(self):
        # Выпускаем физическую карту — только если счёт успешно создан
        if not self.open_debit_card_account_response:
            return

        account = self.open_debit_card_account_response.account

        self.issue_physical_card_response = (
            self.cards_gateway_client.issue_physical_card(
                account_id=account.id,
                user_id=self.create_user_response.user.id,  # фикс: user берём из create_user_response
            )
        )


class IssuePhysicalCardScenarioUser(LocustBaseUser):
    tasks = [IssuePhysicalCardSequentialTaskSet]
