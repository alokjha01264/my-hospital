# Healthcare Backend API

[cite\_start]This project is a backend system for a healthcare application built with Django and Django REST Framework. [cite: 1] [cite\_start]It provides a secure API for managing user authentication, patient records, and doctor information. [cite: 2]

## Features

  * [cite\_start]**User Authentication**: Secure user registration and login using JWT (JSON Web Tokens). [cite: 2, 4]
  * [cite\_start]**Patient Management**: Authenticated users can perform CRUD (Create, Read, Update, Delete) operations on patient records they own. [cite: 8, 9, 10]
  * [cite\_start]**Doctor Management**: Authenticated users can add and manage doctor records. [cite: 11, 12, 13]
  * [cite\_start]**Patient-Doctor Mapping**: Assign doctors to patients and manage these relationships. [cite: 13, 14, 15]

## Tech Stack

  * [cite\_start]**Backend**: Django, Django REST Framework (DRF) [cite: 3]
  * [cite\_start]**Database**: PostgreSQL [cite: 3]
  * [cite\_start]**Authentication**: djangorestframework-simplejwt [cite: 4]
  * [cite\_start]**Environment Variables**: python-dotenv [cite: 30, 31]

## Prerequisites

  * [cite\_start]Python 3.11+ [cite: 27]
  * [cite\_start]PostgreSQL [cite: 28]
  * [cite\_start]Git [cite: 28]

## Getting Started

Follow these steps to set up and run the project locally.

### 1\. Clone the Repository

```bash
git clone <your-repository-url>
cd healthcare-backend
```

### 2\. Set Up a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies.

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

Install all the required Python packages using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4\. Configure Environment Variables

Create a `.env` file in the project root directory. This file will store your sensitive configurations.

```bash
# .env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=healthdb
DB_USER=healthuser
DB_PASSWORD=healthpass
DB_HOST=127.0.0.1
DB_PORT=5432
```

### 5\. Set Up the PostgreSQL Database

Make sure your PostgreSQL server is running. Create a new database and user that matches the credentials in your `.env` file.

### 6\. Run Database Migrations

[cite\_start]Apply the database schema by running the following commands: [cite: 37, 51]

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7\. Create a Superuser (Optional)

[cite\_start]You can create a superuser to access the Django admin panel: [cite: 37]

```bash
python manage.py createsuperuser
```

### 8\. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

Here is a list of the available API endpoints.

### Authentication

  * [cite\_start]`POST /api/auth/register/`: Register a new user. [cite: 6]
  * [cite\_start]`POST /api/auth/login/`: Log in to get a JWT token. [cite: 7]

### Patients

  * [cite\_start]`POST /api/patients/`: Add a new patient. [cite: 8]
  * [cite\_start]`GET /api/patients/`: Get a list of patients created by the authenticated user. [cite: 9]
  * [cite\_start]`GET /api/patients/<id>/`: Get details of a specific patient. [cite: 9]
  * [cite\_start]`PUT /api/patients/<id>/`: Update a patient's details. [cite: 10]
  * [cite\_start]`DELETE /api/patients/<id>/`: Delete a patient. [cite: 10]

### Doctors

  * [cite\_start]`POST /api/doctors/`: Add a new doctor. [cite: 11]
  * [cite\_start]`GET /api/doctors/`: Get a list of all doctors. [cite: 11]
  * [cite\_start]`GET /api/doctors/<id>/`: Get details of a specific doctor. [cite: 12]
  * [cite\_start]`PUT /api/doctors/<id>/`: Update a doctor's details. [cite: 12]
  * [cite\_start]`DELETE /api/doctors/<id>/`: Delete a doctor. [cite: 13]

### Mappings

  * [cite\_start]`POST /api/mappings/`: Assign a doctor to a patient. [cite: 13]
  * [cite\_start]`GET /api/mappings/`: Get all patient-doctor mappings. [cite: 14]
  * [cite\_start]`GET /api/mappings/<patient_id>/`: Get all doctors for a specific patient. [cite: 14]
  * [cite\_start]`DELETE /api/mappings/delete/<id>/`: Remove a patient-doctor mapping. [cite: 15]

## Testing the API

[cite\_start]You can use a tool like Postman to test the API endpoints. [cite: 17, 28] For protected routes, you will need to include the JWT access token in the `Authorization` header.

**Example Header**:

```
Authorization: Bearer <your_jwt_token>
```