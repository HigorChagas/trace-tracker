from datetime import datetime

from sqlalchemy import ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class Error(Base):
    __tablename__ = "error"

    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(ForeignKey("user.id"))
    name: Mapped[str]
    context: Mapped[str] = mapped_column(String(500))
    severity: Mapped[str] = mapped_column(String(25))
    language: Mapped[str] = mapped_column(String(25))
    create_date: Mapped[datetime] = mapped_column(insert_default=func.now())

    user: Mapped["User"] = relationship(back_populates="errors")
