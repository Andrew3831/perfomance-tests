from locust import task, events
from locust.env import Environment

from clients.grpc.gateway.locust import GatewayGRPCTaskSet
from seeds.scenarios.existing_user_get_operations import ExistingUserGetOperationsSeedsScenario
from seeds.schema.result import SeedUserResult
from tools.locust.user import LocustBaseUser


# ---------------------------
# Хук: выполняем сидинг перед нагрузкой
# ---------------------------
@events.init.add_listener
def init(environment: Environment, **kwargs):
    # Генерируем тестовые данные: пользователи, счета, карты, операции
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()

    # Загружаем сидинговые данные и сохраняем в окружение
    environment.seeds = seeds_scenario.load()


# ---------------------------
# Сценарий пользователя
# ---------------------------
class GetOperationsTaskSet(GatewayGRPCTaskSet):
    seed_user: SeedUserResult

    def on_start(self) -> None:
        super().on_start()
        # Выбираем случайного пользователя для текущего виртуального пользователя
        self.seed_user = self.user.environment.seeds.get_random_user()

    @task(2)
    def get_accounts(self):
        # Получение списка счетов пользователя
        self.accounts_gateway_client.get_accounts(user_id=self.seed_user.user_id)

    @task(4)
    def get_operations(self):
        # Пользователь чаще обновляет список операций
        account_id = self.seed_user.credit_card_accounts[0].account_id
        self.operations_gateway_client.get_operations(account_id=account_id)

    @task(3)
    def get_operations_summary(self):
        # Получение агрегированной статистики по операциям
        account_id = self.seed_user.credit_card_accounts[0].account_id
        self.operations_gateway_client.get_operations_summary(account_id=account_id)


# ---------------------------
# Класс виртуального пользователя
# ---------------------------
class GetOperationsScenarioUser(LocustBaseUser):
    tasks = [GetOperationsTaskSet]
