from locust import task

from clients.http.gateway.locust import GatewayHTTPSequentialTaskSet
from clients.http.gateway.users.schema import CreateUserResponseSchema
from clients.http.gateway.accounts.schema import OpenDebitCardAccountResponseSchema
from clients.http.gateway.cards.schema import IssuePhysicalCardResponseSchema
from tools.locust.user import LocustBaseUser


class IssuePhysicalCardSequentialTaskSet(GatewayHTTPSequentialTaskSet):
    """
    Последовательный сценарий выпуска физической дебетовой карты новым пользователем.

    Шаги сценария:
    1. Создание нового пользователя.
    2. Открытие дебетового счёта.
    3. Выпуск физической карты, привязанной к счёту.

    Все вызовы выполняются последовательно благодаря SequentialTaskSet.
    """

    create_user_response: CreateUserResponseSchema | None = None
    open_debit_account_response: OpenDebitCardAccountResponseSchema | None = None
    issue_physical_card_response: IssuePhysicalCardResponseSchema | None = None

    @task
    def create_user(self):
        """
        Шаг 1: Создание нового пользователя.
        Создаёт пользователя через UsersGatewayClient.
        """
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_debit_account(self):
        """
        Шаг 2: Открытие дебетового счёта.
        Для нового пользователя создаётся дебетовый счёт.
        """
        if not self.create_user_response:
            return

        self.open_debit_account_response = (
            self.accounts_gateway_client.open_debit_card_account(
                user_id=self.create_user_response.user.id
            )
        )

    @task
    def issue_physical_card(self):
        """
        Шаг 3: Выпуск физической карты.
        Физическая карта выпускается через CardsGatewayClient.
        """
        if not self.open_debit_account_response:
            return

        account = self.open_debit_account_response.account

        self.issue_physical_card_response = (
            self.cards_gateway_client.issue_physical_card(
                user_id=self.create_user_response.user.id,
                account_id=account.id
            )
        )


class IssuePhysicalCardScenarioUser(LocustBaseUser):
    """
    Пользователь Locust, выполняющий сценарий выпуска физической карты.

    Используется в нагрузочном тесте.
    """
    tasks = [IssuePhysicalCardSequentialTaskSet]
