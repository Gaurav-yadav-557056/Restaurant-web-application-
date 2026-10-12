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

```text
restaurant_project/
├── manage.py
├── requirements.txt
├── restaurant_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── food/
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
