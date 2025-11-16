#!/usr/bin/env python3

from __future__ import annotations
import grpc

from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import (
    OpenDebitCardAccountRequest,
    OpenDebitCardAccountResponse,
)
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub

from tools.fakers import fake


def main() -> None:
    channel = grpc.insecure_channel("localhost:9003")

    users_stub = UsersGatewayServiceStub(channel)
    accounts_stub = AccountsGatewayServiceStub(channel)

    # --- Создание пользователя ---
    create_req = CreateUserRequest(
        email=fake.email(),
        last_name=fake.last_name(),
        first_name=fake.first_name(),
        middle_name=fake.middle_name(),
        phone_number=fake.phone_number(),
    )

    create_resp: CreateUserResponse = users_stub.CreateUser(create_req)
    print("Create user response:", create_resp)

    user_id = create_resp.user.id

    # --- Открытие дебетового счёта ---
    open_req = OpenDebitCardAccountRequest()
    open_req.user_id = user_id

    open_resp: OpenDebitCardAccountResponse = accounts_stub.OpenDebitCardAccount(open_req)
    print("\nOpen debit card account response:", open_resp)


if __name__ == "__main__":
    main()

