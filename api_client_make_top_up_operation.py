from clients.http.gateway.users.client import build_users_gateway_http_client
from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.operations.client import build_operations_gateway_http_client

# Инициализируем API-клиенты
users_gateway_client = build_users_gateway_http_client()
accounts_gateway_client = build_accounts_gateway_http_client()
operations_gateway_client = build_operations_gateway_http_client()

# Шаг 1: Создаем пользователя
create_user_response = users_gateway_client.create_user()
print('Create user response:', create_user_response)

# Извлекаем user_id
user_id = create_user_response['user']['id']

# Шаг 2: Открываем дебетовый счет
open_debit_card_account_response = accounts_gateway_client.open_debit_card_account(user_id)
print('Open debit card account response:', open_debit_card_account_response)

# Извлекаем account_id и virtual card id
account_id = open_debit_card_account_response['account']['id']
virtual_card_id = open_debit_card_account_response['account']['cards'][0]['id']

# Шаг 3: Выполняем операцию пополнения счета
top_up_response = operations_gateway_client.make_top_up_operation(card_id=virtual_card_id, account_id=account_id)
print('Make top up operation response:', top_up_response)