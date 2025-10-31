import time
import httpx

# Устанавливаем большой тайм-аут на случай долгой задержки
TIMEOUT_SECONDS = 30  # устанавливаем тайм-аут в 30 секунд

# Данные для создания пользователя
create_user_payload = {
    "email": f"user-{int(time.time())}@example.com",  # уникальный email на основе текущего времени
    "lastName": "Иванов",
    "firstName": "Иван",
    "middleName": "Иванович",
    "phoneNumber": "+79991234567"
}

# Выполнение POST-запроса на создание пользователя с большим тайм-аутом
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload, timeout=TIMEOUT_SECONDS)

# Проверка статуса ответа
if create_user_response.status_code == 200:
    user_data = create_user_response.json()
    # Получаем user.id из вложенного объекта 'user'
    user_id = user_data["user"]["id"]
else:
    print(f"Ошибка при создании пользователя. Статус-код: {create_user_response.status_code}. Сообщение: {create_user_response.text}")
    exit(1)

# Данные для открытия депозитного счёта
deposit_payload = {
    "user_id": user_id  # добавляем user.id в запрос
}

# Выполнение POST-запроса на открытие депозитного счёта с большим тайм-аутом
deposit_response = httpx.post("http://localhost:8003/api/v1/accounts/open-deposit-account", json=deposit_payload, timeout=TIMEOUT_SECONDS)

# Проверка статуса ответа
if deposit_response.status_code == 200:
    deposit_data = deposit_response.json()
    print("\nJSON-ответ от сервера с данными о созданном счёте:")
    print(deposit_data)
    print("\nСтатус-код ответа:", deposit_response.status_code)
else:
    print(f"Ошибка при открытии депозитного счёта. Статус-код: {deposit_response.status_code}. Сообщение: {deposit_response.text}")