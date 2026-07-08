# 🏠 Taskly API

A Django REST Framework backend for managing tasks within shared houses. Users can create houses, manage members, organize task lists, assign tasks, upload attachments, and track task completion.

Built with **Django**, **Django REST Framework**, and deployed on **Render**.

---

## 🚀 Live API

**Base URL**

https://taskly-app-0v4q.onrender.com/api/

### Available Endpoints

| Endpoint | Description |
|----------|-------------|
| `/api/` | API Root |
| `/api/accounts/` | User & Profile APIs |
| `/api/house/` | House APIs |
| `/api/task/` | Task, Task Lists & Attachments |
| `/admin/` | Django Admin |

---

# ✨ Features

## 👤 User & Profile Management

- User profiles linked to Django's built-in User model
- Upload profile images
- Associate users with houses

## 🏠 House Management

- Create houses
- Assign house managers
- Manage house members
- Track completed and incomplete tasks
- Store house images and descriptions

## 📋 Task Lists

- Create multiple task lists per house
- Track creation dates
- Organize household work

## ✅ Task Management

- Create tasks
- Mark tasks as completed
- Record who created and completed tasks
- Track completion dates

## 📎 Attachments

- Upload files to tasks
- Store supporting documents or images

## 🔒 Permissions

- Read-only access for anonymous users
- Authenticated users can create and manage resources

---

# 🗂 Data Models

### Profile

- User
- Image
- House

### House

- Name
- Image
- Description
- Manager
- Points
- Task statistics

### TaskList

- House
- Name
- Description
- Status
- Created by
- Created on

### Task

- Task List
- Name
- Description
- Status
- Created by
- Completed by
- Created on
- Completed on

### Attachment

- Task
- Uploaded file
- Created on

---

# ⚙️ Local Installation

Clone the repository

```bash
git clone https://github.com/gragra-kj/Taskly_App.git
```

Move into the project

```bash
cd Taskly_App/src
```

Create a virtual environment

```bash
python3 -m venv venv
```

Activate it

Linux/macOS

```bash
source ../venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Apply migrations

```bash
python manage.py migrate
```

Create a superuser (optional)

```bash
python manage.py createsuperuser
```

Run the development server

```bash
python manage.py runserver
```

---

# 🔗 Example API Endpoints

### Accounts

```
GET /api/accounts/
```

### Houses

```
GET /api/house/
POST /api/house/
```

### Task Lists

```
GET /api/task/tasklists/
POST /api/task/tasklists/
```

### Tasks

```
GET /api/task/tasks/
POST /api/task/tasks/
```

### Attachments

```
GET /api/task/attachments/
POST /api/task/attachments/
```

---

# 🛠 Technologies Used

- Python 3.12
- Django 5.2
- Django REST Framework
- SQLite (Development)
- PostgreSQL (Production)
- Gunicorn
- WhiteNoise
- Render

---

# 📁 Project Structure

```
src/
├── users/
├── house/
├── task/
├── background_jobs/
├── taskful_api/
├── media/
├── manage.py
└── requirements.txt
```

---

# 🌍 Deployment

The project is deployed on **Render** using:

- Gunicorn
- PostgreSQL
- WhiteNoise for static files
- Environment variables for sensitive settings

Live API:

https://taskly-app-0v4q.onrender.com/api/

---

# 📄 Disclaimer

This project was developed while following **The Complete Python Django REST API Development Bootcamp** on Udemy. The original project structure and concepts are based on the course content. Additional modifications, deployment configuration, bug fixes, and improvements were implemented independently for learning and portfolio purposes.
