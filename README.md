# Taskly API

Taskly is a Django REST Framework-powered backend project that allows registered users to manage tasks within shared houses. It supports authentication, house membership, task list creation, and detailed task tracking, including attachments.

---

## 🎓 Project Features

### 🏡 User & Profile Management

* Each user has an extended `Profile` linked to Django's `User` model.
* Users can upload a profile image.
* Profiles are linked to a house (optional).

### 🏠 House Management

* Create and manage shared houses.
* Assign a single profile as the house manager.
* Houses track the number of completed and not completed tasks.

### 🍎 Task & Task List Management

* Houses contain `TaskLists`, each with many `Tasks`.
* Task lists and tasks track who created and completed them.
* Tasks can be marked as **Completed** or **Not Completed**.
* Attachments (e.g. images or files) can be added to tasks.

### 🔑 Authentication

* Token or OAuth2 authentication can be added (based on implementation).
* Secure access control through DRF permissions and custom validation.

---

## 🔢 Data Models Overview

### 👤 `Profile`

* Extends `User`
* Fields: `image`, `house`

### 🏠 `House`

* Fields: `name`, `image`, `description`, `manager`, `points`, `task counts`
* Relationships: `members` (Profile), `lists` (TaskList)

### 📂 `TaskList`

* Belongs to a `House`
* Fields: `name`, `description`, `created_on`, `status`
* Relationships: `created_by` (Profile), `tasks` (Task)

### ✅ `Task`

* Belongs to a `TaskList`
* Fields: `name`, `description`, `status`, `created_on`, `completed_on`
* Relationships: `created_by`, `completed_by` (Profile)

### 📁 `Attachment`

* Belongs to a `Task`
* Fields: `data (file)`, `created_on`

---

## ⚙️ Setup Instructions

1. **Clone the repository**
2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```
5. **Run the server**

   ```bash
   python manage.py runserver
   ```
6. **Create superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

---

## 🔗 API Endpoints

These depend on your registered routers, but typical examples include:

* `GET /api/accounts/profiles/`
* `GET /api/house/`
* `GET /api/task/tasklists/`
* `POST /api/task/tasks/`
* `POST /api/task/attachments/`

Authentication may be required depending on your `permissions.py` setup.

---

## 🌐 Technologies Used

* Python 3.13
* Django 5.1.7
* Django REST Framework
* OAuth2 / Token Authentication (configurable)
* File uploads with custom paths

---


## 📄 Disclaimer

This project was developed as part of the [The Complete Python Django REST API Development Bootcamp](https://www.udemy.com/course/the-complete-python-django-rest-api-development-bootcamp/learn/lecture/24335966#overview) course on Udemy. All core structure and logic are based on the course content by the original instructor. Additional modifications and implementations have been made for learning and portfolio purposes.

---



