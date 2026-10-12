<<<<<<< HEAD
# My Restaurant — Django Starter Project

A beginner-friendly restaurant ordering website built with Django.

## Features
- Home page and food menu
- Food categories and food detail pages
- Search menu items
- Admin panel to manage food and categories
- Add/edit/delete food through staff-only pages
- Session-based shopping cart
- Quantity updates and item removal
- Checkout creates an order and order-item price snapshots
- Order confirmation page
- Basic validation and 404 handling

## Important limitations
- This is a learning/demo project, not production-ready.
- Checkout does **not** charge money. Do not collect real card details.
- The checkout flow is a simple guest checkout. Add authentication, payment gateway integration, email notifications, automated tests, and production security before deploying publicly.
- The app uses SQLite for easy local setup. PostgreSQL can be added later.

## Run on Windows (PowerShell or CMD)

1. Extract the ZIP.
2. Open a terminal in the folder containing `manage.py`.
3. Create and activate a virtual environment:

   ```powershell
   py -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use Command Prompt instead:
   ```cmd
   venv\Scripts\activate.bat
   ```

4. Install Django:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Create database tables:

   ```powershell
   python manage.py makemigrations food
   python manage.py migrate
   ```

6. Create an admin account:

   ```powershell
   python manage.py createsuperuser
   ```

7. Start the server:

   ```powershell
   python manage.py runserver
   ```

8. Open:
   - Website: http://127.0.0.1:8000/
   - Menu: http://127.0.0.1:8000/food/
   - Admin: http://127.0.0.1:8000/admin/

## First use
1. Sign in to `/admin/`.
2. Add one or more categories.
3. Add food items and mark them available.
4. Visit `/food/`, add items to the cart, and test checkout.

## Project structure
=======
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
>>>>>>> b63050aac046732dc90b22bf41348c2dd57fca01

```text
restaurant_project/
├── manage.py
<<<<<<< HEAD
├── requirements.txt
=======
├── db.sqlite3
>>>>>>> b63050aac046732dc90b22bf41348c2dd57fca01
├── restaurant_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── food/
<<<<<<< HEAD
    ├── migrations/
    │   └── __init__.py
    ├── templates/food/
    ├── models.py
    ├── forms.py
    ├── cart.py
    ├── views.py
    ├── urls.py
    └── admin.py
```
=======
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
>>>>>>> b63050aac046732dc90b22bf41348c2dd57fca01
