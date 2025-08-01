# Django

# firstproject - Build Log & Setup Guide (with django-tailwind)

This document outlines all the steps taken to set up this Django project, including the integration of Tailwind CSS via the `django-tailwind` package. It serves as a reference for understanding the project structure and for recreating the setup.

---

## 📋 Table of Contents

1. Initial Django Project Setup  
2. Tailwind CSS Integration (`django-tailwind`)  
3. Creating Templates and Views  
4. Summary of Changes from an Untouched Project  
5. Development Workflow  
6. Command Reference  

---

## 1. 🛠️ Initial Django Project Setup

### a. Create Virtual Environment

```bash
# Create the virtual environment
python3 -m venv .venv

# Activate it (macOS/Linux)
source .venv/bin/activate

# On Windows
.venv\Scripts\activate
```

### b. Install Django and Create Project

```bash
pip install django
django-admin startproject firstproject .
```

### c. Create requirements.txt

```bash
pip freeze > requirements.txt
```

---

## 2. 🎨 Tailwind CSS Integration (via django-tailwind)

### a. Install Required Packages

```bash
pip install django-tailwind django-browser-reload
pip freeze > requirements.txt
```

### b. Update `settings.py`

```python
# firstproject/settings.py

INSTALLED_APPS = [
    ...
    'django.contrib.staticfiles',
    'tailwind',
    'theme',
    'django_browser_reload',
]

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]

MIDDLEWARE = [
    ...
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'theme/templates'],
        'APP_DIRS': True,
        ...
    },
]

STATIC_URL = 'static/'
STATICFILES_DIRS = [ BASE_DIR / 'theme/static' ]
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

### c. Initialize Tailwind

```bash
python manage.py tailwind init
```

### d. Install Tailwind Frontend Dependencies

```bash
python manage.py tailwind install
```

---

## 3. 🧩 Creating Templates and Views

### a. Create Base Template

**`theme/templates/base.html`**:

```html
{% load static tailwind_tags %}
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Project</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {% tailwind_css %}
</head>
<body class="bg-gray-50 font-serif">
    {% block content %}{% endblock %}
</body>
</html>
```

### b. Create Index View

**`theme/views.py`**:

```python
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

### c. Create URL Routes

**`theme/urls.py`**:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

**`firstproject/urls.py`**:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', include('theme.urls')),
]
```

---

## 4. 🔄 Summary of Changes from a Fresh Project

### `firstproject/settings.py`

- `INSTALLED_APPS`: added `'tailwind'`, `'theme'`, `'django_browser_reload'`
- `MIDDLEWARE`: added `"django_browser_reload.middleware.BrowserReloadMiddleware"`
- `TEMPLATES.DIRS`: updated with `BASE_DIR / 'theme/templates'`
- `STATICFILES_DIRS`: added development static path
- `STATIC_ROOT`: added for production
- `TAILWIND_APP_NAME` and `INTERNAL_IPS` added

### `firstproject/urls.py`

- Imported `include`
- Added routes for `theme.urls` and `django_browser_reload.urls`

### `theme/`

- Created `views.py` with `index` view
- Created `urls.py` for internal routing
- Added `base.html` and `index.html` under `templates`

---

## 5. 🚀 Development Workflow

Run two terminals during development:

### Terminal 1 – Tailwind Watcher

```bash
python manage.py tailwind start
```

### Terminal 2 – Django Server

```bash
python manage.py runserver
```

---

## 6. 🧾 Command Reference

| Command | Description |
|--------|-------------|
| `django-admin startproject <name> .` | Start new Django project |
| `python manage.py startapp <name>` | Create new Django app |
| `python manage.py runserver` | Run development server |
| `python manage.py migrate` | Apply DB migrations |
| `python manage.py makemigrations` | Create migration files |
| `python manage.py collectstatic` | Gather static files for production |
| `pip install <package>` | Install Python package |
| `python manage.py tailwind init` | Initialize Tailwind and theme app |
| `python manage.py tailwind install` | Install Tailwind dependencies |
| `python manage.py tailwind start` | Run Tailwind compiler in watch mode |
| `python manage.py tailwind build` | Build Tailwind for production |

---

✅ You're now ready to build modern, styled Django apps using Tailwind!
