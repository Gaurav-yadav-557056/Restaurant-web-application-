# Restaurant-web-application-
#  Django Restaurant Management System

A web-based restaurant application developed using **Python and Django**. This project aims to simplify restaurant operations by displaying food items, managing menu information, and building a foundation for an online food ordering system.

##  Features

- **Food Menu:** Display available food items.
- **Food Details:** Store food names, prices, and availability.
- **Dynamic Web Pages:** Render restaurant data using Django templates.
- **Database Integration:** Manage food information through Django models.
- **Admin Panel:** Manage restaurant data using Django's built-in administration interface.
- **Scalable Architecture:** Designed to support future features such as shopping carts, customer accounts, and online payments.

##  Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS
- **Database:** SQLite (Django default, unless configured otherwise)
- **Version Control:** Git and GitHub

##  Project Structure

```text
restaurant_project/
├── manage.py
├── db.sqlite3
├── restaurant_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── food/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    └── templates/
        └── food_list.html
```

*Note: The structure above is illustrative. Your actual folders and files may differ.*

##  Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Navigate to the project directory

```bash
cd YOUR-REPOSITORY
```

Navigate into the directory containing `manage.py` if necessary.

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Django

```bash
pip install django
```

If a `requirements.txt` file is available, install the project dependencies instead:

```bash
pip install -r requirements.txt
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open the application in your browser:

http://127.0.0.1:8000/

##  Usage

1. Start the Django development server.
2. Open the application in your browser.
3. Visit the configured food menu URL to view available food items.
4. Use the Django admin panel to manage food records if admin access is configured.

To create an administrator account:

```bash
python manage.py createsuperuser
```

Then open http://127.0.0.1:8000/admin/ .

##  Future Improvements

- Customer registration and login
- Food search and category filtering
- Shopping cart functionality
- Order placement and order tracking
- Online payment integration
- Responsive user interface
- Restaurant dashboard and sales reports

##  Project Objective

The objective of this project is to gain practical experience in Django development, including models, views, templates, URL routing, database operations, and full-stack web application development.

## Author

**Gaurav Yadav**

B.Tech in Information Technology | PSIT Kanpur

## License

This project is available for educational and learning purposes. Add a license file if you intend to distribute it under specific terms.
