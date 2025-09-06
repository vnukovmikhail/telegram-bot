from datetime import datetime
from sqlalchemy import BigInteger, String, DateTime
from sqlalchemy.orm import mapped_column, Mapped

from bot.db.models import BaseModel

class UserModel(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True, index=True)
    user_name: Mapped[str] = mapped_column(String(64), nullable=True)
    full_name: Mapped[str] = mapped_column(String(128), nullable=True)
    registered_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())