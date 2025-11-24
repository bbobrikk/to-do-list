from datetime import date
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import CheckConstraint
from application.core.connection import Base


class TaskORM(Base):

    __tablename__ = "Tasks"

    task_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    status: Mapped[str]
    deadline: Mapped[date]
    created_at: Mapped[date]

    __table_args__ = (
        CheckConstraint("status in ('done', 'running')", "CHK_status_valid"),
        CheckConstraint("deadline >= created_at", "CHK_date_valid"),
    )
