from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)

    created_tasks = relationship(
        "Task",
        foreign_keys="Task.created_by",
        back_populates="creator"
    )

    
    assigned_tasks = relationship(
        "Task",
        foreign_keys="Task.assigned_to",
        back_populates="assignee"
    )


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)

    created_by = Column(Integer, ForeignKey("users.id"))
    assigned_to = Column(Integer, ForeignKey("users.id"))

    creator = relationship(
        "User",
        foreign_keys=[created_by],
        back_populates="created_tasks"
    )

    assignee = relationship(
        "User",
        foreign_keys=[assigned_to],
        back_populates="assigned_tasks"
    )
