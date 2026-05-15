from datetime import datetime
from typing import Optional

from sqlalchemy import Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class User(Base):
    __tablename__ = "user"

    id = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    fullname: Mapped[Optional[str]]
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password: Mapped[str] = mapped_column(String(255))
    create_date: Mapped[datetime] = mapped_column(insert_default=func.now())

    errors: Mapped[list["Error"]] = relationship(back_populates="user")
