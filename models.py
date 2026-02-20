#  # SQLAlchemy models (Users, Tasks, Interviews, Activity)
# from sqlalchemy import Column, Integer, String, DateTime
# from database import Base
# from datetime import datetime

# class Task(Base):
#     __tablename__ = "tasks"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String)
#     priority = Column(String)
#     status = Column(String, default="Pending")
#     assigned_to = Column(String)
#     completion_time = Column(DateTime, nullable=True)


# class Interview(Base):
#     __tablename__ = "interviews"

#     id = Column(Integer, primary_key=True, index=True)
#     candidate_name = Column(String)
#     datetime = Column(String)
#     mode = Column(String)

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    role = Column(String)  # 'employer' / 'virtual_hr'
    email = Column(String, unique=True)
    password = Column(String)

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    priority = Column(String)
    assigned_to = Column(Integer, ForeignKey("users.id"))
    status = Column(String, default="Pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)

class Interview(Base):
    __tablename__ = "interviews"
    id = Column(Integer, primary_key=True, index=True)
    candidate_name = Column(String)
    date_time = Column(DateTime)
    mode = Column(String)  # Voice/Video/Chat
    scheduled_by = Column(Integer, ForeignKey("users.id"))

class Activity(Base):
    __tablename__ = "activity"
    id = Column(Integer, primary_key=True, index=True)
    action_type = Column(String)
    description = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)