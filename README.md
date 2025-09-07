# 🏥 Healthcare Backend

A Django REST Framework–based backend for managing healthcare operations.  
This project was developed as part of my internship assignment.  

---

## ⚙️ Features

- **User Management** – authentication and user accounts  
- **Doctor Management** – CRUD APIs for managing doctors  
- **Patient Management** – CRUD APIs for patients  
- **Patient–Doctor Mappings** – assign doctors to patients and manage relationships  

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework  
- **Database:** PostgreSQL (can be swapped with SQLite for testing)  
- **Authentication:** JWT (JSON Web Tokens)  
- **Other:** Python 3.9+  

---

## 📂 Project Structure
---
```bash
healthcare_backend/
├─ .env
├─ manage.py
├─ requirements.txt
├─ README.md
├─ config/           # Django project settings
├─ apps/
│  ├─ users/         # Authentication & user management
│  ├─ core/          # Core entities: patients, doctors
│  └─ mappings/      # Patient–doctor relationships

```

## 🚀 Getting Started

Clone the repository  
```bash
git clone https://github.com/<your-username>/healthcare-backend.git

```

```bash
Navigate to project folder

cd healthcare-backend
```

```bash
Create a virtual environment

python -m venv venv
```
```bash
Activate the virtual environment (Linux/MacOS)

source venv/bin/activate
```
```bash
Activate the virtual environment (Windows PowerShell)

venv\Scripts\activate
```
```bash
Install dependencies

pip install -r requirements.txt
```
```bash
Apply migrations

python manage.py migrate
```
```bash
Create a superuser (optional, for admin access)

python manage.py createsuperuser
```
```bash
Run the development server

python manage.py runserver
```
