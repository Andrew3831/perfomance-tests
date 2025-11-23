from pydantic import BaseModel, Field


class SeedCardResult(BaseModel):
    """
    Результат выпуска карты.

    Attributes:
        card_id (str): ID созданной карты.
    """
    card_id: str


class SeedOperationResult(BaseModel):
    """
    Результат выполнения операции.

    Attributes:
        operation_id (str): ID созданной операции.
    """
    operation_id: str


class SeedAccountResult(BaseModel):
    """
    Результат генерации счёта, включая созданные карты и операции.

    Attributes:
        account_id (str): ID созданного счёта.
        physical_cards (list[SeedCardResult]): Выпущенные физические карты.
        virtual_cards (list[SeedCardResult]): Выпущенные виртуальные карты.
        top_up_operations (list[SeedOperationResult]): Список пополнений.
        purchase_operations (list[SeedOperationResult]): Список покупок.
        transfer_operations (list[SeedOperationResult]): Список переводов.
        cash_withdrawal_operations (list[SeedOperationResult]): Список снятий наличных.
    """

    account_id: str

    physical_cards: list[SeedCardResult] = Field(default_factory=list)
    virtual_cards: list[SeedCardResult] = Field(default_factory=list)

    top_up_operations: list[SeedOperationResult] = Field(default_factory=list)
    purchase_operations: list[SeedOperationResult] = Field(default_factory=list)

    transfer_operations: list[SeedOperationResult] = Field(default_factory=list)
    cash_withdrawal_operations: list[SeedOperationResult] = Field(default_factory=list)


class SeedUserResult(BaseModel):
    """
    Результат генерации пользователя, включая его счета и операции.

    Attributes:
        user_id (str): ID пользователя.
        deposit_accounts (list[SeedAccountResult])
        savings_accounts (list[SeedAccountResult])
        debit_card_accounts (list[SeedAccountResult])
        credit_card_accounts (list[SeedAccountResult])
    """
    user_id: str

    deposit_accounts: list[SeedAccountResult] = Field(default_factory=list)
    savings_accounts: list[SeedAccountResult] = Field(default_factory=list)
    debit_card_accounts: list[SeedAccountResult] = Field(default_factory=list)
    credit_card_accounts: list[SeedAccountResult] = Field(default_factory=list)


class SeedsResult(BaseModel):
    """
    Результат полного сидинга данных.

    Attributes:
        users (list[SeedUserResult]): Список сгенерированных пользователей.
    """
    users: list[SeedUserResult] = Field(default_factory=list)

    def get_next_user(self) -> SeedUserResult:
        """Возвращает и удаляет первого пользователя из списка."""
        return self.users.pop(0)

    def get_random_user(self) -> SeedUserResult:
        """Возвращает случайного пользователя из списка без удаления."""
        import random
        return random.choice(self.users)
