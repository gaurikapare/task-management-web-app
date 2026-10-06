from typing import Optional

from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models import Task
from app.schemas import TaskCreate, TaskUpdate


def get_tasks(db: Session, search: Optional[str] = None, status: Optional[str] = None, priority: Optional[str] = None):
    query = db.query(Task)

    if search:
        pattern = f"%{search.strip()}%"
        query = query.filter(or_(Task.title.ilike(pattern), Task.description.ilike(pattern)))

    if status:
        query = query.filter(Task.status == status.upper())

    if priority:
        query = query.filter(Task.priority == priority.upper())

    return query.order_by(Task.created_at.desc()).all()


def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def create_task(db: Session, payload: TaskCreate):
    task = Task(
        title=payload.title,
        description=payload.description,
        status=payload.status,
        priority=payload.priority,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def update_task(db: Session, task: Task, payload: TaskUpdate):
    for field, value in payload.model_dump(exclude_unset=True).items():
        if value is not None:
            setattr(task, field, value)

    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task: Task):
    db.delete(task)
    db.commit()
