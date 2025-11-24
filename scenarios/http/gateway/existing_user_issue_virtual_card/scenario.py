from locust import task, events
from locust.env import Environment

from clients.http.gateway.locust import GatewayHTTPTaskSet
from seeds.scenarios.existing_user_issue_virtual_card import ExistingUserIssueVirtualCardSeedsScenario
from seeds.schema.result import SeedUserResult
from tools.locust.user import LocustBaseUser


# --- Выполняем сидинг до старта нагрузки ---
@events.init.add_listener
def init(environment: Environment, **kwargs):
    seeds_scenario = ExistingUserIssueVirtualCardSeedsScenario()

    # Генерация данных
    seeds_scenario.build()

    # Загружаем набор подготовленных пользователей
    environment.seeds = seeds_scenario.load()


# --- TaskSet сценария ---
class IssueVirtualCardTaskSet(GatewayHTTPTaskSet):
    seed_user: SeedUserResult

    def on_start(self) -> None:
        super().on_start()

        # Берём случайного пользователя
        self.seed_user = self.user.environment.seeds.get_random_user()

    @task(5)
    def get_accounts(self):
        # ⚠ API требует user_id, поэтому передаём его
        self.accounts_gateway_client.get_accounts(
            user_id=self.seed_user.user_id
        )

    @task(1)
    def issue_virtual_card(self):
        # Выпуск новой виртуальной карты для дебетового счёта пользователя
        # Передаём обязательный user_id и account_id
        self.cards_gateway_client.issue_virtual_card(
            user_id=self.seed_user.user_id,
            account_id=self.seed_user.debit_card_accounts[0].account_id
        )


# --- Виртуальный пользователь ---
class IssueVirtualCardScenarioUser(LocustBaseUser):
    tasks = [IssueVirtualCardTaskSet]
