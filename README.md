Role-Based Task Management System
1 Tech Stack

Python

FastAPI

SQLAlchemy

SQLite

JWT Authentication

HTML (Basic Frontend)

2 Features

JWT-based authentication

Role-based access control

Admin can create and assign tasks

Editor can update assigned tasks

Viewer can only view assigned tasks

Secure API endpoints

Swagger documentation available

3 User Roles

Admin

Create, read, update, delete any task

Assign tasks to users

View all users

Editor

View assigned tasks

Update assigned tasks

Cannot delete

Viewer

View assigned tasks only

Cannot create, update, delete

4 Setup Instructions

Clone repository

Create virtual environment

Install dependencies

pip install -r requirements.txt


Run server

uvicorn main:app --reload


Access Swagger:

http://127.0.0.1:8000/docs

5 API Endpoints

Authentication:

POST /auth/register

POST /auth/login

Task Management:

POST /tasks (Admin only)

GET /tasks

GET /tasks/{task_id}

PUT /tasks/{task_id}

DELETE /tasks/{task_id}

