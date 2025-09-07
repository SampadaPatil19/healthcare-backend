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

healthcare_backend/
├─ .env
├─ manage.py
├─ requirements.txt
├─ README.md
├─ config/ # Django project settings
├─ apps/
│ ├─ users/ # Authentication & user management
│ ├─ core/ # Core entities: patients, doctors
│ └─ mappings/ # Patient–doctor relationships

yaml
Copy code

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/healthcare-backend.git
cd healthcare-backend
2. Create Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Configure Environment
Create a .env file in the root folder:

ini
Copy code
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/healthcare_db
(You can also use SQLite for quick testing by updating settings.py.)

5. Apply Migrations
bash
Copy code
python manage.py migrate
6. Create Superuser
bash
Copy code
python manage.py createsuperuser
7. Run Server
bash
Copy code
python manage.py runserver
📡 API Endpoints
🔑 Authentication (Users App)
POST /api/users/register/ – Register new user

POST /api/users/login/ – Obtain JWT token

👨‍⚕️ Doctors (Core App)
POST /api/doctors/ – Add new doctor (authenticated)

GET /api/doctors/ – List all doctors

GET /api/doctors/<id>/ – Retrieve doctor by ID

PUT /api/doctors/<id>/ – Update doctor (authenticated)

DELETE /api/doctors/<id>/ – Delete doctor (authenticated)

🧑‍🤝‍🧑 Patients (Core App)
POST /api/patients/ – Add new patient (authenticated)

GET /api/patients/ – List all patients

GET /api/patients/<id>/ – Retrieve patient by ID

PUT /api/patients/<id>/ – Update patient (authenticated)

DELETE /api/patients/<id>/ – Delete patient (authenticated)

🔗 Patient–Doctor Mappings (Mappings App)
POST /api/mappings/ – Assign doctor to patient (authenticated)

GET /api/mappings/ – List all mappings

GET /api/mappings/<patient_id>/ – List all doctors for a patient

DELETE /api/mappings/delete/<id>/ – Remove doctor from patient (authenticated)

🧪 Testing
Run all tests:

bash
Copy code
python manage.py test
🤝 Contribution
This project was created as an internship assignment.
Suggestions and improvements are always welcome!
