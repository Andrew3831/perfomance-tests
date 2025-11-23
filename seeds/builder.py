from seeds.schema.result import SeedOperationResult, SeedCardResult, SeedAccountResult, SeedUserResult, SeedsResult


class SeedsBuilder:
    """
    SeedsBuilder отвечает за генерацию тестовых данных согласно плану SeedsPlan.
    Он создаёт пользователей, счета, карты и операции, используя HTTP/gRPC клиенты.
    """

    def __init__(self, users_gateway_client, cards_gateway_client, accounts_gateway_client, operations_gateway_client):
        """
        Инициализация билдеров.

        Args:
            users_gateway_client: Клиент API пользователей.
            cards_gateway_client: Клиент API карт.
            accounts_gateway_client: Клиент API счетов.
            operations_gateway_client: Клиент API операций.
        """
        self.users_gateway_client = users_gateway_client
        self.cards_gateway_client = cards_gateway_client
        self.accounts_gateway_client = accounts_gateway_client
        self.operations_gateway_client = operations_gateway_client

    # -------------------- КАРТЫ --------------------

    def build_physical_card_result(self, user_id: str, account_id: str) -> SeedCardResult:
        """Выпускает физическую карту для пользователя и счёта."""
        response = self.cards_gateway_client.issue_physical_card(
            user_id=user_id,
            account_id=account_id
        )
        return SeedCardResult(card_id=response.card.id)

    def build_virtual_card_result(self, user_id: str, account_id: str) -> SeedCardResult:
        """
        Выпускает виртуальную карту для пользователя и счёта.

        Вызывает API: issue_virtual_card
        """
        response = self.cards_gateway_client.issue_virtual_card(
            user_id=user_id,
            account_id=account_id
        )
        return SeedCardResult(card_id=response.card.id)

    # -------------------- ОПЕРАЦИИ --------------------

    def build_top_up_operation_result(self, card_id: str, account_id: str) -> SeedOperationResult:
        """Создаёт операцию пополнения (top-up)."""
        response = self.operations_gateway_client.make_top_up_operation(
            card_id=card_id,
            account_id=account_id
        )
        return SeedOperationResult(operation_id=response.operation.id)

    def build_purchase_operation_result(self, card_id: str, account_id: str) -> SeedOperationResult:
        """Создаёт операцию покупки."""
        response = self.operations_gateway_client.make_purchase_operation(
            card_id=card_id,
            account_id=account_id
        )
        return SeedOperationResult(operation_id=response.operation.id)

    def build_transfer_operation_result(self, card_id: str, account_id: str) -> SeedOperationResult:
        """
        Создаёт операцию перевода средств.

        Вызывает API: make_transfer_operation
        """
        response = self.operations_gateway_client.make_transfer_operation(
            card_id=card_id,
            account_id=account_id
        )
        return SeedOperationResult(operation_id=response.operation.id)

    def build_cash_withdrawal_operation_result(self, card_id: str, account_id: str) -> SeedOperationResult:
        """
        Создаёт операцию снятия наличных.

        Вызывает API: make_cash_withdrawal_operation
        """
        response = self.operations_gateway_client.make_cash_withdrawal_operation(
            card_id=card_id,
            account_id=account_id
        )
        return SeedOperationResult(operation_id=response.operation.id)

    # -------------------- СЧЕТА --------------------

    def build_savings_account_result(self, user_id: str) -> SeedAccountResult:
        """Открывает сберегательный счёт."""
        response = self.accounts_gateway_client.open_savings_account(user_id=user_id)
        return SeedAccountResult(account_id=response.account.id)

    def build_deposit_account_result(self, user_id: str) -> SeedAccountResult:
        """Открывает депозитный счёт."""
        response = self.accounts_gateway_client.open_deposit_account(user_id=user_id)
        return SeedAccountResult(account_id=response.account.id)

    def build_debit_card_account_result(self, plan, user_id: str) -> SeedAccountResult:
        """
        Открывает дебетовый счёт и выполняет связанные действия:
        - Выпуск физ. карт
        - Выпуск виртуальных карт
        - Пополнения
        - Покупки
        - Переводы
        - Снятия наличных
        """
        response = self.accounts_gateway_client.open_debit_card_account(user_id=user_id)

        account_id = response.account.id
        main_card_id = response.account.cards[0].id

        return SeedAccountResult(
            account_id=account_id,

            physical_cards=[
                self.build_physical_card_result(user_id, account_id)
                for _ in range(plan.physical_cards.count)
            ],

            virtual_cards=[
                self.build_virtual_card_result(user_id, account_id)
                for _ in range(plan.virtual_cards.count)
            ],

            top_up_operations=[
                self.build_top_up_operation_result(main_card_id, account_id)
                for _ in range(plan.top_up_operations.count)
            ],

            purchase_operations=[
                self.build_purchase_operation_result(main_card_id, account_id)
                for _ in range(plan.purchase_operations.count)
            ],

            transfer_operations=[
                self.build_transfer_operation_result(main_card_id, account_id)
                for _ in range(plan.transfer_operations.count)
            ],

            cash_withdrawal_operations=[
                self.build_cash_withdrawal_operation_result(main_card_id, account_id)
                for _ in range(plan.cash_withdrawal_operations.count)
            ]
        )

    def build_credit_card_account_result(self, plan, user_id: str) -> SeedAccountResult:
        """
        Открывает кредитный счёт и выполняет связанные действия:
        - виртуальные/физические карты
        - покупки/пополнения
        - переводы/снятия наличных
        """
        response = self.accounts_gateway_client.open_credit_card_account(user_id=user_id)

        account_id = response.account.id
        main_card_id = response.account.cards[0].id

        return SeedAccountResult(
            account_id=account_id,

            physical_cards=[
                self.build_physical_card_result(user_id, account_id)
                for _ in range(plan.physical_cards.count)
            ],

            virtual_cards=[
                self.build_virtual_card_result(user_id, account_id)
                for _ in range(plan.virtual_cards.count)
            ],

            top_up_operations=[
                self.build_top_up_operation_result(main_card_id, account_id)
                for _ in range(plan.top_up_operations.count)
            ],

            purchase_operations=[
                self.build_purchase_operation_result(main_card_id, account_id)
                for _ in range(plan.purchase_operations.count)
            ],

            transfer_operations=[
                self.build_transfer_operation_result(main_card_id, account_id)
                for _ in range(plan.transfer_operations.count)
            ],

            cash_withdrawal_operations=[
                self.build_cash_withdrawal_operation_result(main_card_id, account_id)
                for _ in range(plan.cash_withdrawal_operations.count)
            ]
        )

    # -------------------- ПОЛЬЗОВАТЕЛЬ --------------------

    def build_user(self, plan):
        """
        Создаёт пользователя и его счета согласно заданному плану.
        """
        response = self.users_gateway_client.create_user()
        user_id = response.user.id

        return SeedUserResult(
            user_id=user_id,
            savings_accounts=[self.build_savings_account_result(user_id) for _ in range(plan.savings_accounts.count)],
            deposit_accounts=[self.build_deposit_account_result(user_id) for _ in range(plan.deposit_accounts.count)],
            debit_card_accounts=[
                self.build_debit_card_account_result(plan.debit_card_accounts, user_id)
                for _ in range(plan.debit_card_accounts.count)
            ],
            credit_card_accounts=[
                self.build_credit_card_account_result(plan.credit_card_accounts, user_id)
                for _ in range(plan.credit_card_accounts.count)
            ]
        )

    # -------------------- КОРНЕВОЙ МЕТОД --------------------

    def build(self, plan):
        """
        Запускает процесс сидинга:
        - создаёт пользователей
        - каждому создаёт счета, карты, операции
        """
        return SeedsResult(users=[self.build_user(plan.users) for _ in range(plan.users.count)])
