# 🛠️ Django Maintenance Mode Middleware

A lightweight and admin-controlled **maintenance mode system** for Django projects.  
Allows staff users to toggle the site into a user-friendly “Under Construction” state,  
with optional secret bypass for developers. ✨

[![Built with Django](https://img.shields.io/badge/Built%20with-Django-092E20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)

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
| ![Before Maintenance](https://github.com/user-attachments/assets/e2c7e845-60ef-4f4a-9027-d4595f739915) | ![Maintenance-Page](https://github.com/user-attachments/assets/88d3f8b4-349d-499b-9332-327b0f70a499)
| ![Admin Panel](https://github.com/user-attachments/assets/ba80436c-4adc-4f18-9d82-c5be40406205) | ![Secret-Key](https://github.com/user-attachments/assets/dc5f93b0-53ef-404f-b43a-e5e4d874f6bf)

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
