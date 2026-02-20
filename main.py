# #FASTAPI app entry

# from fastapi import FastAPI, Depends
# from fastapi.middleware.cors import CORSMiddleware
# from sqlalchemy.orm import Session
# from database import engine, SessionLocal
# import models
# from datetime import datetime
# from pydantic import BaseModel

# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # --------- Pydantic Schema ---------

# class TaskCreate(BaseModel):
#     title: str
#     priority: str
#     assigned_to: str

# # --------- Dependency ---------

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # --------- Routes ---------

# @app.post("/create-task")
# def create_task(task: TaskCreate, db: Session = Depends(get_db)):
#     new_task = models.Task(**task.dict())
#     db.add(new_task)
#     db.commit()
#     db.refresh(new_task)
#     return new_task


# @app.get("/tasks")
# def get_tasks(db: Session = Depends(get_db)):
#     return db.query(models.Task).all()


# @app.put("/update-task/{task_id}")
# def update_task(task_id: int, status: str, db: Session = Depends(get_db)):
#     task = db.query(models.Task).filter(models.Task.id == task_id).first()

#     if not task:
#         return {"error": "Task not found"}

#     task.status = status

#     if status == "Completed":
#         task.completion_time = datetime.now()

#     db.commit()
#     db.refresh(task)
#     return task

from fastapi import FastAPI, Depends
from database import init_db, SessionLocal
from routers import tasks, interviews, activity
from fastapi.middleware.cors import CORSMiddleware

init_db()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks.router)
app.include_router(interviews.router)
app.include_router(activity.router)

# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # production में specific origin use करो
    allow_methods=["*"],
    allow_headers=["*"],
)