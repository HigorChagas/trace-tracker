from pydantic import BaseModel, EmailStr, Field, SecretStr


class Register(BaseModel):
    email: EmailStr = Field(..., min_length=10)
    password: SecretStr = Field(..., min_length=5, max_length=100)
    name: str


class Login(BaseModel):
    email: EmailStr = Field(..., min_length=10)
    password: SecretStr = Field(..., min_length=5, max_length=100)
