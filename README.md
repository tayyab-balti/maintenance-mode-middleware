# 🛠️ Django Maintenance Mode Middleware

A lightweight and admin-controlled **maintenance mode system** for Django projects.  
Allows staff users to toggle the site into a user-friendly “Under Construction” state,  
with optional secret bypass for developers. ✨

[![Built with Django](https://img.shields.io/badge/Built%20with-Django-092E20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![MIT License](https://img.shields.io/github/license/tayyab-balti/maintenance-mode-middleware?style=for-the-badge)](LICENSE)

---

## 📌 Features

- ✅ Middleware-based global site lock for visitors
- ✅ Admin toggle for **Maintenance ON/OFF**
- ✅ Optional note and duration display
- ✅ **Secret bypass** for developers (via URL key)
- ✅ Clean UI for the maintenance page
- ✅ Staff users always have full access

---

## 📸 Screenshots

| Admin Toggle | Maintenance Page |
|--------------|------------------|
| ![Admin Panel](assets/admin-toggle.png) | ![Maintenance Page](assets/maintenance-view.png) |

> ℹ️ *(You can add your own screenshots in the `assets/` folder!)*

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/tayyab-balti/maintenance-mode-middleware.git
cd maintenance-mode-middleware
```

### 2. Setup & Run

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Migrate database
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

## 🧠 What I Learned

- Django middleware customization  
- Secure session and request handling  
- Admin UX restrictions and model design  
- Secrets management using `python-decouple`  
- Clean UI/UX even for backend tools  

## 💡 Use Cases

- Deploying changes without user disruption  
- Showing planned maintenance notices  
- Locking early-access or pre-launch sites  
- Graceful handling of downtime in production  
