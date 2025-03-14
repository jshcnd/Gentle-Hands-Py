# Gentle Hands Project

This is a Django-based web application for user registration, login, and homepage functionality. The project is configured to use a PostgreSQL database. This project is a collaborative effort developed during our on-the-job training (OJT) to meet the requirements of our client.

## Group Members

- **Andrea** - UX/UI Designer
- **Elmar** - Lead Developer
- **Hanns** - Database Administrator
- **Jessie** - Frontend Developer
- **Justin** - QA Engineer
- **Kim** - Frontend Developer
- **Rhoen** - Project Manager

## Project Structure

```
myproject/
    db.sqlite3
    manage.py
    accounts/
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
        __pycache__/
            __init__.cpython-311.pyc
            admin.cpython-311.pyc
            apps.cpython-311.pyc
            models.cpython-311.pyc
            views.cpython-311.pyc
        migrations/
            __init__.py
            __pycache__/
                ...
        templates/
            dashboard.html
            home.html
            login.html
            logout.html
            register.html
    myproject/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
        __pycache__/
            ...
```

## Features

- User Registration
- User Login
- User Logout
- Homepage
- Dashboard

## Setup Instructions

1. **Clone the repository:**

    ```sh
    git clone <repository-url>
    cd myproject
    ```

2. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Configure the database:**

    Update the `DATABASES` setting in `myproject/settings.py` to match your PostgreSQL configuration.

4. **Run migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

7. **Access the application:**

    Open your web browser and go to `http://localhost:8000`.

## Application URLs

- **Homepage:** `/`
- **Register:** `/register/`
- **Login:** `/login/`
- **Dashboard:** `/dashboard/`
- **Logout:** `/logout/`

## Custom User Model

The project uses a custom user model defined in `accounts/models.py`. The custom user model extends Django's `AbstractUser`.

## Templates

The HTML templates for the application are located in the `accounts/templates` directory.

- `home.html`: Homepage template
- `register.html`: Registration template
- `login.html`: Login template
- `dashboard.html`: Dashboard template
- `logout.html`: Logout template

## Admin

The custom user model is registered with the Django admin site in `accounts/admin.py`.

## License

This project is licensed under the MIT License.
