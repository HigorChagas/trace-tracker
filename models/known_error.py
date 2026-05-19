from datetime import datetime

from sqlalchemy import Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class KnownError(Base):
    __tablename__ = "known_errors"

    id = mapped_column(Integer, primary_key=True)
    error_name: Mapped[str]
    summary: Mapped[str] = mapped_column(Text)
    language: Mapped[str] = mapped_column(String(25))
    create_date: Mapped[datetime] = mapped_column(insert_default=func.now())
