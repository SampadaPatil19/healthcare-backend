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


## 🚀 Getting Started

Clone the repository  
```bash
git clone https://github.com/<your-username>/healthcare-backend.git
Navigate to project folder

```bash
Copy code
cd healthcare-backend
Create a virtual environment

```bash
Copy code
python -m venv venv
Activate the virtual environment (Linux/MacOS)

```bash
Copy code
source venv/bin/activate
Activate the virtual environment (Windows PowerShell)

```bash
Copy code
venv\Scripts\activate
Install dependencies

```bash
Copy code
pip install -r requirements.txt
Apply migrations

```bash
Copy code
python manage.py migrate
Create a superuser (optional, for admin access)

```bash
Copy code
python manage.py createsuperuser
Run the development server

```bash
Copy code
python manage.py runserver
