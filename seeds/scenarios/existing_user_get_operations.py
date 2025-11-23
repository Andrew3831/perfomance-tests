from seeds.scenario import SeedsScenario
from seeds.schema.plan import (
    SeedsPlan,
    SeedUsersPlan,
    SeedAccountsPlan,
    SeedOperationsPlan,
)


class ExistingUserGetOperationsSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга для существующего пользователя,
    который просматривает список операций и статистику по кредитному счёту.

    Генерируем:
    - 300 пользователей
    - каждому 1 кредитный счёт
    - для счёта создаём:
        * 5 операций покупки
        * 1 операцию пополнения
        * 1 операцию снятия наличных
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        План сидинга — описание того, что нужно сгенерировать.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,
                credit_card_accounts=SeedAccountsPlan(
                    count=1,
                    purchase_operations=SeedOperationsPlan(count=5),
                    top_up_operations=SeedOperationsPlan(count=1),
                    cash_withdrawal_operations=SeedOperationsPlan(count=1),
                ),
            )
        )

    @property
    def scenario(self) -> str:
        """
        Имя сценария. Используется для генерации файла:
        dumps/existing_user_get_operations_seeds.json
        """
        return "existing_user_get_operations"


if __name__ == "__main__":
    """
    Запуск:
    python -m seeds.scenarios.existing_user_get_operations
    """
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()
