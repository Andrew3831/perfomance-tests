import time
import httpx

# Максимальное время ожидания ответа от сервера (в секундах)
TIMEOUT_SECONDS = 120

# Шаг 1: Создаём пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload, timeout=TIMEOUT_SECONDS)

# Проверяем успешность создания пользователя
if create_user_response.is_success:
    create_user_response_data = create_user_response.json()
    user_id = create_user_response_data["user"]["id"]
else:
    print(f"Ошибка при создании пользователя. Статус-код: {create_user_response.status_code}, "
          f"Текст ошибки: {create_user_response.text}")
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

# Проверяем успешность открытия кредитного счёта
if open_credit_card_account_response.is_success:
    open_credit_card_account_response_data = open_credit_card_account_response.json()
    account_id = open_credit_card_account_response_data["account"]["id"]
else:
    print(f"Ошибка при открытии кредитного счёта. Статус-код: {open_credit_card_account_response.status_code}, "
          f"Текст ошибки: {open_credit_card_account_response.text}")
    exit(1)

# Шаг 3: Получаем тарифный документ
get_tariff_document_response = httpx.get(
    f"http://localhost:8003/api/v1/documents/tariff-document/{account_id}",
    timeout=TIMEOUT_SECONDS
)

# Проверяем успешность получения тарифа
if get_tariff_document_response.is_success:
    get_tariff_document_response_data = get_tariff_document_response.json()
    print("Tariff Document Response:", get_tariff_document_response_data)
    print("Tariff Document Status Code:", get_tariff_document_response.status_code)
else:
    print(f"Ошибка при получении тарифного документа. Статус-код: {get_tariff_document_response.status_code}, "
          f"Текст ошибки: {get_tariff_document_response.text}")

# Шаг 4: Получаем контракт
get_contract_document_response = httpx.get(
    f"http://localhost:8003/api/v1/documents/contract-document/{account_id}",
    timeout=TIMEOUT_SECONDS
)

# Проверяем успешность получения контракта
if get_contract_document_response.is_success:
    get_contract_document_response_data = get_contract_document_response.json()
    print("Contract Document Response:", get_contract_document_response_data)
    print("Contract Document Status Code:", get_contract_document_response.status_code)
else:
    print(f"Ошибка при получении контракта. Статус-код: {get_contract_document_response.status_code}, "
          f"Текст ошибки: {get_contract_document_response.text}")