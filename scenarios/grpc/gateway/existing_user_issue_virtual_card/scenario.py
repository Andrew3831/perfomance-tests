from locust import task, events
from locust.env import Environment

from clients.grpc.gateway.locust import GatewayGRPCTaskSet
from seeds.scenarios.existing_user_issue_virtual_card import ExistingUserIssueVirtualCardSeedsScenario
from seeds.schema.result import SeedUserResult
from tools.locust.user import LocustBaseUser


@events.init.add_listener
def init(environment: Environment, **kwargs):
    seeds_scenario = ExistingUserIssueVirtualCardSeedsScenario()
    seeds_scenario.build()
    environment.seeds = seeds_scenario.load()


class IssueVirtualCardTaskSet(GatewayGRPCTaskSet):
    seed_user: SeedUserResult

    def on_start(self):
        super().on_start()
        self.seed_user = self.user.environment.seeds.get_random_user()

    @task(3)
    def get_accounts(self):
        self.accounts_gateway_client.get_accounts(
            user_id=self.seed_user.user_id
        )

    @task(1)
    def issue_virtual_card(self):
        account = self.seed_user.debit_card_accounts[0]

        self.cards_gateway_client.issue_virtual_card(
            account_id=account.account_id,
            user_id=self.seed_user.user_id,
        )


class IssueVirtualCardScenarioUser(LocustBaseUser):
    tasks = [IssueVirtualCardTaskSet]
