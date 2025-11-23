from pydantic import BaseModel, Field


class SeedCardsPlan(BaseModel):
    """
    План по количеству создаваемых карт (физических или виртуальных).

    Attributes:
        count (int): Сколько карт нужно создать.
    """
    count: int = 0


class SeedOperationsPlan(BaseModel):
    """
    План по количеству создаваемых операций для счёта.

    Attributes:
        count (int): Сколько операций нужно выполнить.
    """
    count: int = 0


class SeedAccountsPlan(BaseModel):
    """
    План генерации счетов одного типа, включая вложенные сущности: карты и операции.

    Attributes:
        count (int): Сколько счетов создать.
        physical_cards (SeedCardsPlan): План по выпуску физических карт.
        virtual_cards (SeedCardsPlan): План по выпуску виртуальных карт.
        top_up_operations (SeedOperationsPlan): План по генерации пополнений.
        purchase_operations (SeedOperationsPlan): План по генерации покупок.
        transfer_operations (SeedOperationsPlan): План по переводу средств.
        cash_withdrawal_operations (SeedOperationsPlan): План по снятию наличных.
    """
    count: int = 0

    physical_cards: SeedCardsPlan = Field(default_factory=SeedCardsPlan)
    virtual_cards: SeedCardsPlan = Field(default_factory=SeedCardsPlan)

    top_up_operations: SeedOperationsPlan = Field(default_factory=SeedOperationsPlan)
    purchase_operations: SeedOperationsPlan = Field(default_factory=SeedOperationsPlan)

    transfer_operations: SeedOperationsPlan = Field(default_factory=SeedOperationsPlan)
    cash_withdrawal_operations: SeedOperationsPlan = Field(default_factory=SeedOperationsPlan)


class SeedUsersPlan(BaseModel):
    """
    План по генерации пользователей и их счетов разных типов.

    Attributes:
        count (int): Количество пользователей.
        deposit_accounts (SeedAccountsPlan): План по депозитным счетам.
        savings_accounts (SeedAccountsPlan): План по сберегательным счетам.
        debit_card_accounts (SeedAccountsPlan): План по дебетовым картам.
        credit_card_accounts (SeedAccountsPlan): План по кредитным картам.
    """

    count: int = 0

    deposit_accounts: SeedAccountsPlan = Field(default_factory=SeedAccountsPlan)
    savings_accounts: SeedAccountsPlan = Field(default_factory=SeedAccountsPlan)
    debit_card_accounts: SeedAccountsPlan = Field(default_factory=SeedAccountsPlan)
    credit_card_accounts: SeedAccountsPlan = Field(default_factory=SeedAccountsPlan)


class SeedsPlan(BaseModel):
    """
    Корневая модель плана для сидинга.

    Attributes:
        users (SeedUsersPlan): План по генерации пользователей.
    """
    users: SeedUsersPlan = Field(default_factory=SeedUsersPlan)
