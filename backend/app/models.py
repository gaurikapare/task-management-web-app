from datetime import datetime, timezone

from sqlalchemy import CheckConstraint, Column, DateTime, Integer, String, Text

from app.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String(20), nullable=False, default="PENDING")
    priority = Column(String(20), nullable=False, default="MEDIUM")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    __table_args__ = (
        CheckConstraint("title <> ''", name="task_title_not_empty"),
        CheckConstraint("status IN ('PENDING', 'IN_PROGRESS', 'COMPLETED')", name="task_status_valid"),
        CheckConstraint("priority IN ('LOW', 'MEDIUM', 'HIGH')", name="task_priority_valid"),
    )
