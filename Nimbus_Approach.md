# 🧩 Nimbus – Project Approach & Design Decisions

## 🎯 Overview
Nimbus is a full-stack web application built with **Django**, **Django REST Framework (DRF)**, and **Chart.js**, designed to demonstrate RESTful API development, third-party API integration, and interactive data visualization.  
It highlights professional coding standards, scalability, and clean UI/UX — all within a compact, recruiter-friendly project.

---

## 🏗️ Architecture & Technology Choices

| Layer | Technology | Reason |
|-------|-------------|--------|
| **Backend** | Django + DRF | Mature, secure, fast development for REST APIs |
| **Database** | SQLite (PostgreSQL-ready via `dj_database_url`) | Lightweight for dev, easily scalable for prod |
| **Auth** | JWT (SimpleJWT) + SessionAuth | Combines token-based security with admin usability |
| **Frontend** | HTML + TailwindCSS + DaisyUI | Simple, responsive, modern dashboard |
| **Visualization** | Chart.js | Quick, flexible JS chart library |
| **Docs** | drf-spectacular + Swagger UI | Auto-generated API documentation |
| **Deployment** | WhiteNoise + Gunicorn | Lightweight static file serving and cloud-ready setup |

---

## ⚙️ Core Functionalities

### 1. Notes CRUD API
- Built using DRF’s `ModelViewSet`
- Supports full Create, Read, Update, Delete operations
- Includes pagination, filtering, and search via query params

### 2. Daily Notes Report
- Aggregates notes by creation date
- Returns daily counts used by Chart.js for live analytics

### 3. GitHub API Integration
- Demonstrates calling external APIs
- Fetches GitHub user data via `https://api.github.com/users/<username>`

### 4. Authentication
- Uses **JWT tokens** (via SimpleJWT)
- Allows secure session-based interaction with frontend
- Ready for expansion with login UI

### 5. Frontend Dashboard
- Built using TailwindCSS + DaisyUI for modern UI
- JavaScript fetches API data for Notes, Analytics, and GitHub integration
- Fully responsive and self-contained (no React/Vue dependencies)

---

## 🧠 Key Design Decisions

- **Separation of Concerns** — API, templates, and static files organized into logical modules.  
- **Scalability** — Database configurable via environment variables.  
- **Security** — `.env` used for secrets; JWT for authentication.  
- **Reusability** — Components like serializers and views kept modular.  
- **Frontend Simplicity** — Vanilla JS handles all interactions, making the app lightweight and fast.  
- **Documentation-first** — Auto-generated Swagger docs ensure instant API understanding.

---

## 🚀 Development Workflow

1. Setup Django + DRF base project  
2. Created Note model and CRUD endpoints  
3. Added analytics route for daily reports  
4. Integrated GitHub API (external data)  
5. Developed frontend dashboard (Tailwind + Chart.js)  
6. Added Swagger API docs  
7. Finalized static management and branding (Nimbus logo, favicon, etc.)

---

## 💡 Challenges & Solutions

| Challenge | Solution |
|------------|-----------|
| Handling CORS and CSRF for fetch requests | Configured `corsheaders` + CSRF token fetch utility |
| Integrating external API (GitHub) | Used DRF `APIView` with robust error handling |
| Chart data formatting | Pre-processed daily counts in backend before sending JSON |
| Static file handling during dev/prod | Used WhiteNoise and `STATICFILES_DIRS` setup for seamless serving |

---

## 🧾 Future Improvements

- Add login/signup UI using JWT
- Include sorting & filters in the dashboard
- Extend analytics with multiple datasets and charts
- Add dark/light theme toggle
- Add test coverage (Pytest + DRF test client)
- Deploy live demo using Render or Railway with PostgreSQL

---



## 👤 Author

**Tejas Kamble**  
📧 [tejaskamble718@gmail.com](mailto:tejaskamble718@gmail.com)   

---

## 🪪 License
This project is licensed under the **MIT License**.  

---

⭐ *If you found Nimbus useful, consider starring it on GitHub!*  
[https://github.com/TejasKamble18/Nimbus](https://github.com/TejasKamble18/Nimbus)
