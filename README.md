Role-Based Task Management System

A FastAPI-based Role-Based Task Management System implementing JWT authentication and strict role-based access control (RBAC).

🚀 Tech Stack

Python

FastAPI

SQLAlchemy

SQLite

JWT (python-jose)

Passlib (bcrypt)

Basic HTML Frontend

🔐 Authentication

JWT-based authentication

Token generated on login

All protected APIs require Bearer token

👥 User Roles
🔹 Admin

Create, read, update, delete any task

Assign tasks to users

View all tasks

🔹 Editor

View assigned tasks

Update assigned tasks

Cannot delete tasks

🔹 Viewer

View assigned tasks only

Cannot create, update, or delete

📋 API Endpoints
Authentication

POST /auth/register

POST /auth/login

Task Management

POST /tasks (Admin only)

GET /tasks

GET /tasks/{task_id}

PUT /tasks/{task_id}

DELETE /tasks/{task_id} (Admin only)

🛠️ Setup Instructions

Clone the repository

Install dependencies

pip install -r requirements.txt


Run the application

uvicorn main:app --reload


Access Swagger documentation:

http://127.0.0.1:8000/docs


