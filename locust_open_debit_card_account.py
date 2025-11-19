from locust import HttpUser, between, task
from tools.fakers import fake


class OpenDebitCardAccountScenarioUser(HttpUser):
    # Пауза между запросами (имитация поведения реального пользователя)
    wait_time = between(1, 3)

    def on_start(self) -> None:
        """
        Создание пользователя перед выполнением задач.
        Отправляем POST /api/v1/users и сохраняем user_id.
        """
        create_user_payload = {
            "email": fake.email(),
            "lastName": fake.last_name(),
            "firstName": fake.first_name(),
            "middleName": fake.middle_name(),
            "phoneNumber": fake.phone_number(),
        }

        response = self.client.post("/api/v1/users", json=create_user_payload)
        response_data = response.json()
        self.user_id = response_data["user"]["id"]

    @task
    def open_debit_card_account(self):
        """
        Основная нагрузочная задача — открыть дебетовый счёт для созданного пользователя.
        Выполняем POST /api/v1/accounts/open-debit-card-account.
        """
        payload = {
            "userId": self.user_id
        }

        self.client.post(
            "/api/v1/accounts/open-debit-card-account",
            json=payload,
            name="/api/v1/accounts/open-debit-card-account"
        )
