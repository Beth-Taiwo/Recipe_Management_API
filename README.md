# recipe_management_api

This project is an introductory setup aimed at familiarizing you with the fundamentals of Django, including environment setup, project creation, and an overview of the default project structure.

## Objective

The primary goal of this project is to gain hands-on experience with Django by:

- Setting up a Django development environment.
- Creating a basic Django project.
- Understanding the default structure of a Django project.

## Prerequisites

- Python installed on your system (version 3.6 or higher recommended).
- pip, the Python package installer, is also required.
- A virtual environment tool, such as `venv` or `virtualenv`, is recommended to manage dependencies.

## Getting Started

Follow these steps to set up your Django development environment and create the recipe_management_api:

### Step 1: Set Up a Virtual Environment

1. Open your terminal.
2. Navigate to the directory where you want to create your project.
3. Run the following command to create a virtual environment:
   ```bash
   python -m venv env
   ```
4. Activate the virtual environment:
   - On macOS and Linux:
     ```bash
     source env/bin/activate
     ```
   - On Windows:
     ```bash
     env\Scripts\activate
     ```

### Step 2: Install Django

With your virtual environment activated, install Django using pip:

```bash
pip install django
```

### Step 3: Create a New Django Project

1. Run the following command to create a new Django project named recipe_management_api:
   ```bash
   django-admin startproject recipe_management_api
   ```
2. Navigate into the newly created `recipe_management_api` directory:
   ```bash
   cd recipe_management_api
   ```

### Step 4: Run the Development Server

1. Start the Django development server to ensure everything is set up correctly:
   ```bash
   python manage.py runserver
   ```
2. Open your web browser and visit `http://127.0.0.1:8000/` to see the default Django welcome page.

## Project Structure Overview

The default structure of a Django project includes the following components:

- **recipe_management_api/**: The main project directory containing:
  - **manage.py**: A command-line utility for interacting with the project.
  - **recipe_management_api/** (inner folder): The actual project code, containing:
    - \***\*init**.py\*\*: Indicates that this directory should be treated as a Python package.
    - **settings.py**: Contains settings and configuration for the project.
    - **urls.py**: Defines the URL patterns for the project.
    - **wsgi.py**: An entry point for WSGI-compatible web servers to serve your project.
    - **asgi.py**: An entry point for ASGI-compatible web servers to serve your project asynchronously.

## Next Steps

Setup and register `api` application

### Step 1: Create a New Django Application

1. Run the following command to create a new Django application named api:
   ```bash
   python3 manage.py startapp api
   ```
2. Go the `recipe_management_api/settings.py` file and register your application by adding the `api` app to your INSTALLED_APPS
   ```bash
   INSTALLED_APPS = [
    ...
    'api',
   ]
   ```

## Testing of user endpoint with Postman

Click on the links below to see a screenshot of the Postman preview

- [POST api/users/](https://drive.google.com/file/d/17YhOcJd__Dbh2VdtgGhcMrggwnzXQvd7/view?usp=drive_link)
- [GET api/users/{id}/](https://drive.google.com/file/d/1xdYKsv1Kyd30TKtabHsYghHVKOLoXvCV/view?usp=sharing)
