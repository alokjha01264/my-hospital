# Healthcare Backend API

A RESTful backend for a healthcare application built with Django and Django REST Framework. This project provides a secure, scalable foundation for managing users, patients, and doctors.

-----

## Features

  * **User Authentication**: Secure user registration and login using JWT (JSON Web Tokens).
  * **Ownership & Permissions**: Users can only view and manage patient records that they have created, ensuring data privacy and security.
  * **Patient Management**: Authenticated users can perform full CRUD (Create, Read, Update, Delete) operations on their patient records.
  * **Doctor Management**: A centralized system to perform CRUD operations on doctor records.
  * **Patient-Doctor Mapping**: Functionality to assign doctors to patients and manage these relationships.
  * **Data Validation**: Built-in validation for incoming data to ensure integrity and provide clear error handling.

-----

## Tech Stack

  * **Backend**: Django, Django REST Framework (DRF)
  * **Database**: PostgreSQL
  * **Database Interaction**: Django ORM
  * **Authentication**: djangorestframework-simplejwt
  * **Environment Variables**: python-dotenv

-----

## Project Structure

The project follows a modular, app-based structure to promote separation of concerns and maintainability:

  * **`accounts`**: Handles user registration and authentication.
  * **`patients`**: Manages all logic related to patient records.
  * **`doctors`**: Manages all logic related to doctor records.
  * **`mappings`**: Manages the relationship between patients and doctors.

-----

## Prerequisites

  * Python 3.11+
  * PostgreSQL
  * Git

-----

## Getting Started

Follow these steps to set up and run the project locally.

### 1\. Clone the Repository

```bash
git clone <your-repository-url>
cd healthcare-backend
```

### 2\. Set Up a Virtual Environment

  * **On macOS/Linux**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
  * **On Windows**:
    ```bash
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

### 3\. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4\. Configure Environment Variables

Create a `.env` file in the project root directory by copying the example:

```bash
# .env
SECRET_KEY=your-super-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=healthdb
DB_USER=healthuser
DB_PASSWORD=healthpass
DB_HOST=127.0.0.1
DB_PORT=5432
```

### 5\. Set Up the PostgreSQL Database

Ensure your PostgreSQL server is running. Create a new database and user that matches the credentials in your `.env` file.

### 6\. Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7\. Run the Development Server

```bash
python manage.py runserver
```

The API will now be available at `http://127.0.0.1:8000/`.

-----

## API Usage Examples

The following examples demonstrate a common workflow.

### 1\. Register a New User

**Request:**

`POST /api/auth/register/`

```json
{
    "username": "testuser",
    "email": "test@example.com",
    "password": "MyStrongPassword123!",
    "password2": "MyStrongPassword123!"
}
```

**Response:** (`201 Created`)

```json
{
    "username": "testuser",
    "email": "test@example.com"
}
```

### 2\. Log In to Get JWT Token

**Request:**

`POST /api/auth/login/`

```json
{
    "username": "testuser",
    "password": "MyStrongPassword123!"
}
```

**Response:** (`200 OK`)

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE3MjUyODc4NDJ9..."
}
```

### 3\. Create a Patient

For this and subsequent requests, you must include the access token in the header:
`Authorization: Bearer <your_access_token>`

**Request:**

`POST /api/patients/`

```json
{
    "name": "Alice",
    "age": 30,
    "gender": "Female",
    "contact_number": "1234567890"
}
```

**Response:** (`201 Created`)

```json
{
    "id": 1,
    "name": "Alice",
    "age": 30,
    "gender": "Female",
    "contact_number": "1234567890",
    "created_by": "testuser"
}
```

### 4\. Create a Doctor

**Request:**

`POST /api/doctors/`

```json
{
    "name": "Dr. John Doe",
    "specialization": "Cardiology",
    "email": "john.doe@example.com",
    "contact_number": "9876543210"
}
```

**Response:** (`201 Created`)

```json
{
    "id": 1,
    "name": "Dr. John Doe",
    "specialization": "Cardiology",
    "email": "john.doe@example.com",
    "contact_number": "9876543210"
}
```

### 5\. Assign a Doctor to a Patient

**Request:**

`POST /api/mappings/`

```json
{
    "patient": 1,
    "doctor": 1
}
```

**Response:** (`201 Created`)

```json
{
    "id": 1,
    "patient": 1,
    "doctor": 1,
    "patient_name": "Alice",
    "doctor_name": "Dr. John Doe",
    "assigned_at": "2025-09-02T14:00:42.123456Z"
}
```