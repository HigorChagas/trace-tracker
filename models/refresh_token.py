from datetime import datetime

from sqlalchemy.orm import mapped_column
from sqlalchemy.orm.base import Mapped
from sqlalchemy.orm.properties import ForeignKey
from sqlalchemy.sql.sqltypes import Integer

from models.base import Base


class RefreshToken(Base):
    __tablename__ = "refresh_token"

    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(ForeignKey("user.id"))
    token_hash: Mapped[str]
    expiration_date: Mapped[datetime]
    revogation_status: Mapped[str]
    device_info: Mapped[bool] = mapped_column(default=False)
