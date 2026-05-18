from pydantic import BaseModel


class Register(BaseModel):
    email: str
    password: str
    name: str


class Login(BaseModel):
    email: str
    password: str
