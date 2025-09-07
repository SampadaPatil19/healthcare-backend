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
---
## 1. Clone the Repository
git clone https://github.com/<your-username>/healthcare-backend.git
cd healthcare-backend
---
## 2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # On Linux/Mac
## venv\Scripts\activate    # On Windows (use this instead)
---
## 3. Install Dependencies
pip install -r requirements.txt
---
## 4. Configure Environment (create .env file in project root)
echo "SECRET_KEY=your_django_secret_key" >> .env
echo "DEBUG=True" >> .env
echo "DATABASE_URL=postgres://user:password@localhost:5432/healthcare_db" >> .env
---
## 5. Apply Migrations
python manage.py migrate
---
## 6. Create Superuser
python manage.py createsuperuser
---
## 7. Run Server
python manage.py runserver

