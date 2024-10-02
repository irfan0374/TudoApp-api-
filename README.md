# Todo API with Django

This project is a Todo API built using Django and Django Rest Framework (DRF). It allows users to manage their tasks with features like adding, updating, viewing, and deleting tasks.

## Features
- **Add new todo**: Authenticated users can add new tasks.
- **List todos**: Retrieve all tasks associated with the authenticated user.
- **Update todo status**: Users can update the status (completed/pending) of a task.
- **Delete todo**: Delete specific tasks.
- **JWT Authentication**: Secure the API with JSON Web Tokens (JWT).

## Prerequisites
- Python 3.12.x
- Django 5.x
- Django Rest Framework
- djangorestframework-simplejwt (for JWT authentication)
- SQLite (default)

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone <your-repo-url>

2.Navigate to the project directory:
cd todoApp

3.Create and activate a virtual environment:
python -m venv env
source env/bin/activate   # On Windows, use `env\Scripts\activate`

4.Install the dependencies:
pip install -r requirements.txt

5.Apply migrations:
python manage.py migrate

6.Create a superuser to access the admin panel:
python manage.py createsuperuser

7.Run the development server:
python manage.py runserver



