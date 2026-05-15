from pydantic import BaseModel


class Message(BaseModel):
    log: str
