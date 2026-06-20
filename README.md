
# GameHub - Full Start (with fixtures)

This project is a complete starter for GameHub with admin-editable categories, sample fixtures and standalone templates.
It includes a small sample dataset you can load after migrations.

## Quick start

1. Create and activate venv:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Make migrations & migrate:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. (Optional) Load sample data (adds categories and two sample games without cover files):
   ```bash
   python manage.py loaddata initial_data.json
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

Open http://127.0.0.1:8000/ and http://127.0.0.1:8000/admin/ to edit categories and games.

