from locust import task

from clients.grpc.gateway.locust import GatewayGRPCTaskSet
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse
from contracts.services.gateway.accounts.rpc_open_deposit_account_pb2 import OpenDepositAccountResponse
from tools.locust.user import LocustBaseUser


class GetAccountsTaskSet(GatewayGRPCTaskSet):
    """
    gRPC TaskSet:
    - create_user
    - open_deposit_account
    - get_accounts
    Все задачи выполняются в любом порядке, поэтому необходимо проверять наличие user_id.
    """

    create_user_response: CreateUserResponse | None = None
    open_deposit_account_response: OpenDepositAccountResponse | None = None

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

