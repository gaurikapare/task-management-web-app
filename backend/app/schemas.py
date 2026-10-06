from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


TaskStatus = Literal["PENDING", "IN_PROGRESS", "COMPLETED"]
TaskPriority = Literal["LOW", "MEDIUM", "HIGH"]


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=150)
    description: Optional[str] = None
    status: TaskStatus = "PENDING"
    priority: TaskPriority = "MEDIUM"

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: Optional[str]) -> Optional[str]:
        if value is None:
            return value
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("Title cannot be empty.")
        return cleaned

    @field_validator("description")
    @classmethod
    def validate_description(cls, value: Optional[str]) -> Optional[str]:
        if value is None:
            return None
        cleaned = value.strip()
        return cleaned or None

    model_config = ConfigDict(from_attributes=True)


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    title: Optional[str] = Field(default=None, min_length=1, max_length=150)
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None


class TaskRead(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime
