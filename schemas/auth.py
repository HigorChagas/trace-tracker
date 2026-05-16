from models.base import Base


class Token(Base):
    access_token: str
    token_type: str


class TokenData(Base):
    email: str | None = None
