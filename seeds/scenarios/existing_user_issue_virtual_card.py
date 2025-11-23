from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan


class ExistingUserIssueVirtualCardSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга для существующего пользователя,
    который входит в приложение, просматривает свои счета
    и выпускает виртуальную карту для дебетового счёта.

    В рамках сидинга создаём:
    - 300 пользователей
    - каждому пользователю открываем 1 дебетовый счёт
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        План сидинга:
        - создать 300 пользователей
        - для каждого пользователя открыть 1 дебетовый счёт
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,
                debit_card_accounts=SeedAccountsPlan(count=1)
            )
        )

    @property
    def scenario(self) -> str:
        """
        Название сценария сидинга.
        Используется как часть имени файла для сохранения результата.
        """
        return "existing_user_issue_virtual_card"


if __name__ == "__main__":
    """
    Позволяет запускать сидинг вручную:
    python -m seeds.scenarios.existing_user_issue_virtual_card
    """
    seeds_scenario = ExistingUserIssueVirtualCardSeedsScenario()
    seeds_scenario.build()
