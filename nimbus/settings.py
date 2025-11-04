# nimbus/settings.py (updated)
from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# Security / env
SECRET_KEY = os.getenv("SECRET_KEY", "unsafe-local-dev-key")
DEBUG = os.environ.get("DEBUG", "False") == "True"
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost").split(",")

# Installed apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "django_filters",
    "drf_spectacular",
    "api",
]

# Middleware (WhiteNoise before others so static files are served)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "nimbus.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "nimbus.wsgi.application"

# ---------------- Safe DB config ----------------
# Use Postgres when DATABASE_URL is provided (Render), otherwise fallback to SQLite for local dev.
db_url = os.environ.get("DATABASE_URL", "") or ""
db_url = db_url.strip()

if db_url:
    # Parse the provided URL and make it production-ready.
    parsed = dj_database_url.parse(db_url)
    # set connection pooling/keep-alive
    parsed["CONN_MAX_AGE"] = 600

    # Put SSL options inside OPTIONS so sqlite driver never sees sslmode
    if "postgres" in db_url or "psql" in db_url:
        parsed.setdefault("OPTIONS", {})
        parsed["OPTIONS"]["sslmode"] = "require"

    DATABASES = {"default": parsed}
else:
    # Local dev fallback - clean sqlite config (no extra keys)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
# ------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# Keep STATICFILES_DIRS only if you have a /static folder in repo root (next to manage.py)
STATICFILES_DIRS = [BASE_DIR / "static"]

# CORS
CORS_ALLOW_ALL_ORIGINS = os.getenv("CORS_ALLOW_ALL_ORIGINS", "True") == "True"

# REST framework
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.OrderingFilter",
        "rest_framework.filters.SearchFilter",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 6,
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
}

# drf-spectacular / Swagger
SPECTACULAR_SETTINGS = {
    "TITLE": "Nimbus API",
    "DESCRIPTION": (
        "Nimbus – A Full-Stack Django + DRF Application with JWT Authentication, "
        "Swagger Docs, and Chart Analytics.\n\n"
        "Features:\n"
        "- CRUD APIs with filters and pagination\n"
        "- JWT Authentication (SimpleJWT)\n"
        "- GitHub API integration\n"
        "- Daily note analytics with Chart.js\n"
        "- Swagger UI powered by drf-spectacular"
    ),
    "VERSION": "1.0.0",
    "CONTACT": {
        "name": "Tejas Kamble",
        "url": "https://socialboostermedia.com/",
        "email": "tejaskamble718@gmail.com",
        "phone": "+91 9373239824",
    },
    "LICENSE": {"name": "MIT License"},
    "TERMS_OF_SERVICE": "https://socialboostermedia.com/terms",
    "SERVE_INCLUDE_SCHEMA": False,
    "SCHEMA_PATH_PREFIX": "/api",
    "SERVE_PERMISSIONS": ["rest_framework.permissions.AllowAny"],
}
