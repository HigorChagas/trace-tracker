from datetime import datetime

from sqlalchemy import ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class ErrorHistory(Base):
    __tablename__ = "error_history"

    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(ForeignKey("user.id"))
    error_name: Mapped[str]
    ia_response: Mapped[str] = mapped_column(Text)
    context: Mapped[str] = mapped_column(Text)
    language: Mapped[str] = mapped_column(String(25))
    create_date: Mapped[datetime] = mapped_column(insert_default=func.now())

    user: Mapped["User"] = relationship(back_populates="errors")
