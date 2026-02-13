Role-Based Task Management System

A FastAPI-based Role-Based Task Management System implementing JWT authentication and strict role-based access control (RBAC).

** Tech Stack

Python

FastAPI

SQLAlchemy

SQLite

JWT (python-jose)

Passlib (bcrypt)

Basic HTML Frontend

** Authentication

JWT-based authentication

Token generated on login

All protected APIs require Bearer token

**** User Roles
** Admin

Create, read, update, delete any task

Assign tasks to users

View all tasks

** Editor

View assigned tasks

Update assigned tasks

Cannot delete tasks

** Viewer

View assigned tasks only

Cannot create, update, or delete

** API Endpoints
Authentication

POST /auth/register

POST /auth/login

Task Management

POST /tasks (Admin only)

GET /tasks

GET /tasks/{task_id}

PUT /tasks/{task_id}

DELETE /tasks/{task_id} (Admin only)

** Setup Instructions

Clone the repository

Install dependencies

pip install -r requirements.txt


Run the application

uvicorn main:app --reload

****  CREDENTIALS :


** Admin

Username: admin1

Password: 1234

Role: admin

ID: 1 

** Editor

Username: editor1

Password: 1234

Role: editor

ID: 2

** Viewer

Username: viewer1

Password: 1234

Role: viewer

ID: 3


Access Swagger documentation:

http://127.0.0.1:8000/docs



# 📊 Database Tables (Current Data Snapshot)

## 🗄️ Users Table

| id | username   | password (hashed) | role   |
|----|------------|-------------------|--------|
| 1  | admin1     | $2b$12$...        | admin  |
| 2  | editor1    | $2b$12$...        | editor |
| 3  | viewer1    | $2b$12$...        | viewer |
| 4  | shashwat   | $2b$12$...        | admin  |
| 5  | shashwat1  | $2b$12$...        | admin  |



---

## 🗄️ Tasks Table

| id | title                                           | description                      | status  | created_at                  | created_by | assigned_to |
|----|-------------------------------------------------|----------------------------------|----------|----------------------------|------------|-------------|
| 1  | Editor Task Only editor should see this         | Only editor should see this      | pending  | 2026-02-13 09:14:21.416027 | 1          | 2           |
| 2  | Viewer Task Only viewer should see this         | Only viewer should see this      | pending  | 2026-02-13 09:14:56.749226 | 1          | 3           |
| 3  | task5                                           | task                             | pending  | 2026-02-13 09:27:20.184621 | 4          | 2           |
| 4  | task22                                          | task                             | pending  | 2026-02-13 10:00:16.422702 | 5          | 2           |

---


