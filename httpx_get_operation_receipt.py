import time
import httpx

# Максимальное время ожидания ответа от сервера (в секундах)
TIMEOUT_SECONDS = 120

# Шаг 1: Создаем пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload, timeout=TIMEOUT_SECONDS)

if create_user_response.is_success:
    create_user_response_data = create_user_response.json()
    user_id = create_user_response_data["user"]["id"]
    print(f"Пользователь создан с ID: {user_id}")
else:
    print(f"Ошибка при создании пользователя. Статус-код: {create_user_response.status_code}, Текст ошибки: {create_user_response.text}")
    exit(1)

# Шаг 2: Открываем кредитный счёт
open_credit_card_account_payload = {
    "userId": user_id
}
open_credit_card_account_response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-credit-card-account",
    json=open_credit_card_account_payload,
    timeout=TIMEOUT_SECONDS
)

if open_credit_card_account_response.is_success:
    open_credit_card_account_response_data = open_credit_card_account_response.json()
    account_id = open_credit_card_account_response_data["account"]["id"]
    card_id = open_credit_card_account_response_data["account"]["cards"][0]["id"]  # Доступ к первой карте
    print(f"Кредитный счёт открыт с ID: {account_id}. Карта создана с ID: {card_id}")
else:
    print(f"Ошибка при открытии кредитного счёта. Статус-код: {open_credit_card_account_response.status_code}, Текст ошибки: {open_credit_card_account_response.text}")
    exit(1)

# Шаг 3: Совершаем покупку
make_purchase_payload = {
    "status": "IN_PROGRESS",
    "amount": 77.99,
    "category": "taxi",
    "cardId": card_id,
    "accountId": account_id  # Уже имеем строку с идентификатором счёта
}
make_purchase_response = httpx.post(
    "http://localhost:8003/api/v1/operations/make-purchase-operation",
    json=make_purchase_payload,
    timeout=TIMEOUT_SECONDS
)

if make_purchase_response.is_success:
    make_purchase_response_data = make_purchase_response.json()
    operation_id = make_purchase_response_data["operation"]["id"]
    print(f"Операция покупки совершена с ID: {operation_id}")
else:
    print(f"Ошибка при совершении покупки. Статус-код: {make_purchase_response.status_code}, Текст ошибки: {make_purchase_response.text}")
    exit(1)

# Шаг 4: Получаем чек по операции
get_receipt_response = httpx.get(
    f"http://localhost:8003/api/v1/operations/operation-receipt/{operation_id}",
    timeout=TIMEOUT_SECONDS
)

if get_receipt_response.is_success:
    receipt_data = get_receipt_response.json()
    print("\nЧЕК ПО ОПЕРАЦИИ:")
    print(receipt_data)
else:
    print(f"Ошибка при получении чека. Статус-код: {get_receipt_response.status_code}, Текст ошибки: {get_receipt_response.text}")