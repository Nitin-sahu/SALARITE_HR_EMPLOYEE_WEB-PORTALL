# Task CRUD endpoints
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Task, Activity
from datetime import datetime

router = APIRouter(prefix="/tasks")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_task(title: str, priority: str, assigned_to: int, db: Session = Depends(get_db)):
    task = Task(title=title, priority=priority, assigned_to=assigned_to)
    db.add(task)
    db.commit()
    db.refresh(task)
    activity = Activity(action_type="Task Created", description=f"Task '{title}' assigned to {assigned_to}")
    db.add(activity)
    db.commit()
    return task

@router.get("/")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()

@router.put("/{task_id}")
def update_task(task_id: int, status: str, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return {"error": "Task not found"}
    task.status = status
    if status == "Completed":
        task.completed_at = datetime.utcnow()
    db.commit()
    activity = Activity(action_type="Task Updated", description=f"Task '{task.title}' status updated to {status}")
    db.add(activity)
    db.commit()
    return task