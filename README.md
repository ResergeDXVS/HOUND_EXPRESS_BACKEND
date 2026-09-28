# 🐕 Hound Express — Backend

## 📖 Description
Backend API for the Hound Express e-commerce project. It is built with Django and Django REST Framework, providing the data and endpoints consumed by the [Hound Express v2 frontend](https://github.com/ResergeDXVS/HOUND_EXPRESS_v2), and is set up to run in a containerized environment with Docker.

## 🛠️ Technologies used
- **Main language:** Python
- **Framework:** Django, Django REST Framework
- **Database:** PostgreSQL (via `psycopg2-binary`)
- **Other tools:** `django-cors-headers` (CORS handling), `python-dotenv` (environment variables), Docker, Docker Compose

## 📂 Project structure
- `app/` — Django project source code
- `Dockerfile` — Image definition for the backend service
- `docker-compose.yml` — Multi-container setup (API + database)
- `requirements.txt` — Python dependencies

## 🚀 Getting started

### Prerequisites
- Docker and Docker Compose installed
- (Alternatively) Python 3 and pip for a local setup without Docker

### Installation and run with Docker
```bash
git clone https://github.com/ResergeDXVS/HOUND_EXPRESS_BACKEND.git
cd HOUND_EXPRESS_BACKEND
docker-compose up --build
```

### Local setup (without Docker)
```bash
git clone https://github.com/ResergeDXVS/HOUND_EXPRESS_BACKEND.git
cd HOUND_EXPRESS_BACKEND
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app/manage.py migrate
python app/manage.py runserver
```

> ⚠️ Remember to configure your environment variables (e.g. database credentials) in a `.env` file, since the project uses `python-dotenv`.

## 📌 Status
Backend developed for the Hound Express e-commerce project.

## 👤 Author
[ResergeDXVS](https://github.com/ResergeDXVS)
