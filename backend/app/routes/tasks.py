from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import TaskCreate, TaskRead, TaskUpdate
from app.services.task_service import create_task, delete_task, get_task_by_id, get_tasks, update_task

router = APIRouter(prefix="/api/tasks", tags=["tasks"])


@router.get("", response_model=list[TaskRead])
def list_tasks(
    search: Optional[str] = Query(default=None, description="Search by title or description"),
    status: Optional[str] = Query(default=None, description="Filter by task status"),
    priority: Optional[str] = Query(default=None, description="Filter by task priority"),
    db: Session = Depends(get_db),
):
    try:
        tasks = get_tasks(db, search=search, status=status, priority=priority)
        return tasks
    except SQLAlchemyError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Unable to load tasks. Please try again.")


@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found.")
    return task


@router.post("", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_new_task(payload: TaskCreate, db: Session = Depends(get_db)):
    try:
        task = create_task(db, payload)
        return task
    except SQLAlchemyError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Unable to create task. Please try again.")


@router.put("/{task_id}", response_model=TaskRead)
def update_existing_task(task_id: int, payload: TaskUpdate, db: Session = Depends(get_db)):
    task = get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found.")

    try:
        updated_task = update_task(db, task, payload)
        return updated_task
    except SQLAlchemyError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Unable to update task. Please try again.")


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_task(task_id: int, db: Session = Depends(get_db)):
    task = get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found.")

    try:
        delete_task(db, task)
    except SQLAlchemyError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Unable to delete task. Please try again.")
    return None
