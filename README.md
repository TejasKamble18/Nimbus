# 🌩️ Nimbus – Full-Stack Django Dashboard App

Nimbus is a modern **Full-Stack Django + Django REST Framework (DRF)** web application featuring **CRUD APIs, data visualization with Chart.js, and third-party API integration**.  
It’s built to demonstrate clean backend design, RESTful architecture, and an interactive front-end dashboard — ideal for showcasing full-stack engineering skills.

---

## 🚀 Features

✅ **Full CRUD Functionality**
- Create, Read, Update, and Delete Notes using Django REST Framework  
- Pagination, filtering, and search support

✅ **Interactive Dashboard**
- Real-time data display using Chart.js  
- Insightful analytics: *Notes per Day* chart

✅ **Third-Party API Integration**
- Live GitHub user lookup (fetches data via public GitHub API)

✅ **Authentication & Security**
- JWT Authentication using Django SimpleJWT  
- CORS enabled for frontend integration  
- CSRF-safe requests in dashboard

✅ **Auto-Generated API Documentation**
- Swagger UI & OpenAPI Schema powered by **drf-spectacular**

✅ **Responsive Frontend**
- Built with **TailwindCSS** + **DaisyUI** for sleek and modern UI

---

## 🏗️ Tech Stack

| Layer | Technology |
|-------|-------------|
| Backend | Python, Django, Django REST Framework |
| Database | SQLite (PostgreSQL ready) |
| Frontend | HTML5, TailwindCSS, DaisyUI, Chart.js |
| Auth | JWT (SimpleJWT), CSRF |
| API Docs | Swagger (drf-spectacular) |
| Deployment Ready | Render / Railway (Gunicorn + WhiteNoise) |

---

## 🧩 Project Structure

nimbus/
├── api/
│ ├── models.py # Database models
│ ├── serializers.py # DRF serializers
│ ├── views.py # API logic (CRUD, reporting, integration)
│ ├── urls.py # API routes
│ └── static/ # App-specific static files
│
├── templates/
│ └── dashboard.html # Interactive frontend dashboard
│
├── static/
│ └── img/
│ └── nimbus-logo.png # App logo
│
├── nimbus/
│ ├── settings.py # Django settings
│ ├── urls.py # Root routing config
│ └── wsgi.py / asgi.py # Entry points
│
├── db.sqlite3 # Default local DB
├── manage.py # Django CLI
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/nimbus.git
cd nimbus

2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate   # on Windows
source venv/bin/activate  # on Mac/Linux

3. Install dependencies
pip install -r requirements.txt

4. Apply migrations
python manage.py migrate

5. Run the development server
python manage.py runserver

6. Access the application

Dashboard: http://127.0.0.1:8000/dashboard/

API Docs: http://127.0.0.1:8000/api/docs/

Admin Panel: http://127.0.0.1:8000/admin/

🧠 Environment Variables (.env)

Create a .env file in your root directory:

SECRET_KEY=django-insecure-your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3
CORS_ALLOW_ALL_ORIGINS=True

📊 API Endpoints
Endpoint	Method	Description
/api/notes/	GET	List all notes
/api/notes/	POST	Create a new note
/api/notes/<id>/	PATCH	Update a note
/api/notes/<id>/	DELETE	Delete a note
/api/report/daily-notes/	GET	Returns daily note analytics
/api/integration/github-user?username=<name>	GET	Fetch GitHub user info
🧰 Commands Cheat Sheet
Command	Description
python manage.py runserver	Start the dev server
python manage.py makemigrations	Create migrations
python manage.py migrate	Apply migrations
python manage.py createsuperuser	Create admin user
python manage.py collectstatic	Gather static files (for production)
🖼️ Screenshot

🧑‍💻 Author

Tejas Kamble

 • 📧 Email

🪪 License

This project is licensed under the MIT License – see the LICENSE file for details.