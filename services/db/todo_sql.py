from datetime import datetime
from services.db.database_client import db
from sqlalchemy.orm import Mapped, mapped_column
class TodoSQL(db.Model):
    __tablename__ = 'todos'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    completed: Mapped[bool] = mapped_column(default=False)
    created: Mapped[datetime] = mapped_column(default=db.func.current_timestamp())
    updated: Mapped[datetime] = mapped_column(default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
