from locust import task, events
from locust.env import Environment

from clients.http.gateway.locust import GatewayHTTPTaskSet
from seeds.scenarios.existing_user_get_operations import ExistingUserGetOperationsSeedsScenario
from seeds.schema.result import SeedUserResult
from tools.locust.user import LocustBaseUser


# Хук инициализации — вызывается перед началом запуска нагрузки
@events.init.add_listener
def init(environment: Environment, **kwargs):
    # Сценарий с HTTP сидингом (теперь внутри него создаётся builder через build_http_seeds_builder)
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()

    # Генерируем данные
    seeds_scenario.build()

    # Загружаем сидинг в память Locust
    environment.seeds = seeds_scenario.load()


# TaskSet — сценарий поведения существующего пользователя
class GetOperationsTaskSet(GatewayHTTPTaskSet):
    seed_user: SeedUserResult

    def on_start(self) -> None:
        super().on_start()
        # Берем случайного подготовленного пользователя
        self.seed_user = self.user.environment.seeds.get_random_user()

    @task(3)
    def get_accounts(self):
        self.accounts_gateway_client.get_accounts(
            user_id=self.seed_user.user_id
        )

    @task(5)
    def get_operations(self):
        self.operations_gateway_client.get_operations(
            account_id=self.seed_user.credit_card_accounts[0].account_id
        )

    @task(2)
    def get_operations_summary(self):
        self.operations_gateway_client.get_operations_summary(
            account_id=self.seed_user.credit_card_accounts[0].account_id
        )


# Виртуальный пользователь
class GetOperationsScenarioUser(LocustBaseUser):
    tasks = [GetOperationsTaskSet]
