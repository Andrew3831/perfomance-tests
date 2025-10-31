import time
import httpx  # Импортируем HTTPX

# Настройка тайм-аута
TIMEOUT_SECONDS = 30  # увеличили тайм-аут до 30 секунд

# Шаг 1. Создание пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",  # Уникальный email с timestamp
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

# Выполнение POST-запроса на создание пользователя с увеличенным тайм-аутом
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload, timeout=TIMEOUT_SECONDS)
create_user_response_data = create_user_response.json()

# Проверка наличия поля 'user' и получение user.id
if "user" in create_user_response_data and "id" in create_user_response_data["user"]:
    user_id = create_user_response_data["user"]["id"]
else:
    print("Ошибка: отсутствуют обязательные поля в ответе!")
    exit(1)

# Шаг 2. Открытие дебетового счёта
open_debit_card_account_payload = {
    "userId": user_id
}

# Выполнение POST-запроса на открытие дебетового счёта с увеличенным тайм-аутом
open_debit_card_account_response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-debit-card-account",
    json=open_debit_card_account_payload,
    timeout=TIMEOUT_SECONDS
)
open_debit_card_account_response_data = open_debit_card_account_response.json()

# Проверка наличия поля 'account' и получение account.id
if "account" in open_debit_card_account_response_data and "id" in open_debit_card_account_response_data["account"]:
    account_id = open_debit_card_account_response_data["account"]["id"]
else:
    print("Ошибка: отсутствуют обязательные поля в ответе!")
    exit(1)

# Шаг 3. Выпуск виртуальной карты
issue_virtual_card_payload = {
    "userId": user_id,
    "accountId": account_id
}

# Выполнение POST-запроса на выпуск виртуальной карты с увеличенным тайм-аутом
issue_virtual_card_response = httpx.post(
    "http://localhost:8003/api/v1/cards/issue-virtual-card",
    json=issue_virtual_card_payload,
    timeout=TIMEOUT_SECONDS
)
issue_virtual_card_response_data = issue_virtual_card_response.json()

# Выводим результат
print("Issue virtual card response:", issue_virtual_card_response_data)
print("Issue virtual card status code:", issue_virtual_card_response.status_code)