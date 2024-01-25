# Django Auth with Serverless CockroachDB Prototype

## Overview

This repository showcases a prototype for a Django authentication app integrated with a serverless CockroachDB backend. The combination of Django and CockroachDB provides scalability and resilience for user authentication in web applications.

## Features

- **Django Authentication**: Utilize Django's built-in authentication system for user management, login, and registration.

- **Serverless CockroachDB**: Employ CockroachDB as the backend database, offering scalability, strong consistency, and fault tolerance.

## Setup

1. **Install Dependencies**:

   ```
   pip install -r requirements.txt
   ```

2. **Database Configuration**:

- Create a serverless CockroachDB cluster and note down connection details.
- Update the DATABASES configuration in settings.py with the CockroachDB connection details.

3. **Apply Migrations**:
   ```
   python manage.py migrate
   ```

4. **Run the Development Server**:
   ```
   python manage.py runserver
   ```

5. **Access the Application**:

- Open your web browser and go to `http://localhost:8000` to interact with the prototype.
