from typing import Optional
from pydantic import BaseModel, EmailStr


# Модель данных пользователя
class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: Optional[str] = None
    phone_number: str


# Запрос на создание пользователя
class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: Optional[str] = None
    phone_number: str


# Ответ с данными созданного пользователя
class CreateUserResponseSchema(BaseModel):
    user: UserSchema