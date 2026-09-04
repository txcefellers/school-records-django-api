# School Records Django API

Django REST Framework API for managing school classes, subjects, students, and marks, with a
student report-card endpoint that computes total and average scores.

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # optional, for /admin/
python manage.py runserver
```

Set `DJANGO_SECRET_KEY` and `DJANGO_DEBUG` environment variables for any non-local deployment
(a development-only fallback secret key is used otherwise).

## Endpoints

- `/admin/` — Django admin, for managing classes, subjects, students, and marks
- `/api/students/<student_id>/report-card/` — GET, returns the student's name, class, marks per
  subject, total score, and average score
