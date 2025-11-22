from locust import task

from clients.http.gateway.locust import GatewayHTTPTaskSet
from clients.http.gateway.users.schema import CreateUserResponseSchema
from clients.http.gateway.accounts.schema import OpenDepositAccountResponseSchema
from tools.locust.user import LocustBaseUser


class GetAccountsTaskSet(GatewayHTTPTaskSet):
    """
    TaskSet, который выполняет:
    - создание пользователя
    - открытие депозитного счёта
    - получение списка счетов
    Все задачи могут выполняться в произвольном порядке.
    """

    create_user_response: CreateUserResponseSchema | None = None
    open_deposit_account_response: OpenDepositAccountResponseSchema | None = None

    @task(2)
    def create_user(self):
        self.create_user_response = self.users_gateway_client.create_user()

    @task(2)
    def open_deposit_account(self):
        if not self.create_user_response:
            return

        self.open_deposit_account_response = (
            self.accounts_gateway_client.open_deposit_account(
                user_id=self.create_user_response.user.id
            )
        )

    @task(6)
    def get_accounts(self):
        if not self.create_user_response:
            return

        self.accounts_gateway_client.get_accounts(
            user_id=self.create_user_response.user.id
        )


class GetAccountsScenarioUser(LocustBaseUser):
    """
    Пользователь, выполняющий произвольные задачи получения аккаунтов.
    """
    tasks = [GetAccountsTaskSet]

