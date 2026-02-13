from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str
    role: str  


class UserLogin(BaseModel):
    username: str
    password: str


class TaskCreate(BaseModel):
    title: str
    description: str
    assigned_to: int



class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    created_by: int
    assigned_to: int
    created_at: datetime

    class Config:
        from_attributes = True



class TokenResponse(BaseModel):
    access_token: str
    token_type: str
