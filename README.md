# Gutenberg Books API

**A RESTful service to query and access Project Gutenberg books.** Built with Django, Django REST Framework, and PostgreSQL.

### Features

- **Filter & Search**:
  - Language (e.g. `en,fr`)
  - Format (MIME types)
  - Topic (subjects or bookshelves; partial, case‑insensitive)
  - Author & Title (partial, case‑insensitive)
  - Project Gutenberg ID
- **Pagination**: 25 books per page with `page` and `page_size` parameters
- **Sorting**: by download count (`ordering=-download_count`) or title
- **Swagger UI**: interactive API docs at `/api/docs/`
- **Nested Data**: authors, subjects, bookshelves, languages, formats included in responses
- **Env‑based Config**: secrets and DB creds via `.env` with `python‑decouple`
- **Dockerized**: run locally with Docker Compose
- **CI/CD**: GitHub Actions for tests and Docker builds

---

### Project Structure
  ```bash
      .
      ├── Dockerfile                     # Container image definition 
      ├── LICENSE
      ├── books                          # Django app (models, serializers, views, filters) 
      │   ├── __init__.py
      │   ├── admin.py
      │   ├── apps.py
      │   ├── filters.py
      │   ├── migrations
      │   │   └── __init__.py
      │   ├── models.py
      │   ├── serializers.py
      │   ├── tests.py
      │   └── views.py
      ├── docker-compose.yml             # Local dev services (API + Postgres) 
      ├── gutenberg                      # Django project (settings, URLs) 
      │   ├── __init__.py
      │   ├── asgi.py
      │   ├── settings.py
      │   ├── urls.py
      │   └── wsgi.py
      ├── manage.py                      # Django CLI 
      └── requirements.txt               # Python dependencies 
      └── .github/workflows/ci.yml       # CI pipeline
  ```
---

### Quick Start (Docker)

1. **Clone repo**
   ```bash
     git clone https://github.com/kishorpawar/gutenberg.git
     cd gutenberg-api
   ```
2. **Configure env**
   ```bash  
    cp .env.example .env
    # Edit .env: set DJANGO_SECRET_KEY, DB_* variables
   ```
3. **Launch**
    ```bash
      docker-compose up --build -d
    ```
4. **Migrations & Superuser**
    ```bash
      docker-compose exec web python manage.py migrate
      docker-compose exec web python manage.py createsuperuser
    ```
5. **Access**
    ```bash
      API: http://localhost:8000/api/books/
      Swagger: http://localhost:8000/api/docs/
    ```

### Running Locally (without Docker)

1. **Set up venv**
    ```bash
      python3 -m venv venv
      source venv/bin/activate
      pip install -r requirements.txt
    ```
2. Configure .env (as above)
3. Run migrations & server
     ```bash
        python manage.py migrate
        python manage.py runserver
     ```
4. Restore dump 
     ```bash
       psql -U <username> -d <dbname> -f ~/Downloads/gutendex.sql >  ~/Downloads/restore.log
     ```
