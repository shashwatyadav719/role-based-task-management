from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine
from models import User, Task
from schema import *
from dependencies import get_db, get_current_user
from auth import hash_password, verify_password, create_access_token
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()
Base.metadata.create_all(bind=engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/auth/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    existing = db.query(User).filter(User.username == user.username).first()

    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    VALID_ROLES = ["admin", "editor", "viewer"]

    if user.role not in VALID_ROLES:
        raise HTTPException(status_code=400, detail="Invalid role")


    hashed = hash_password(user.password)

    new_user = User(
        username=user.username,
        password=hashed,
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully"}



@app.post("/auth/login")
def login(user: UserLogin, db: Session = Depends(get_db), response_model=TokenResponse):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"user_id": db_user.id})
    return {"access_token": token, "token_type": "bearer"}


@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate,
                db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):

    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can create tasks")

    
    assigned_user = db.query(User).filter(User.id == task.assigned_to).first()
    if not assigned_user:
        raise HTTPException(status_code=404, detail="Assigned user not found")

    new_task = Task(
        title=task.title,
        description=task.description,
        created_by=current_user.id,
        assigned_to=task.assigned_to
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db),
              current_user: User = Depends(get_current_user)):

    if current_user.role == "admin":
        return db.query(Task).all()

    return db.query(Task).filter(Task.assigned_to == current_user.id).all()


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int,
                task: TaskUpdate,
                db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):

    db_task = db.query(Task).filter(Task.id == task_id).first()

    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    if current_user.role == "admin" or \
       (current_user.role == "editor" and db_task.assigned_to == current_user.id):

        for key, value in task.dict(exclude_unset=True).items():
            setattr(db_task, key, value)

        db.commit()
        db.refresh(db_task)

        return db_task

    raise HTTPException(status_code=403, detail="Not allowed")



@app.delete("/tasks/{task_id}")
def delete_task(task_id: int,
                db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):

    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not allowed")

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return {"message": "Deleted successfully"}


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_single_task(task_id: int,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if current_user.role == "admin" or task.assigned_to == current_user.id:
        return task

    raise HTTPException(status_code=403, detail="Not allowed")



