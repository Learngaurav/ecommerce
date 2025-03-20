# Flask E-Commerce API

## Overview
This project is a simple **E-Commerce API** built using **Flask**. It allows users to:
- Add and manage products.
- Place orders while ensuring stock availability.
- Store data in a **PostgreSQL** database.
- Utilize **Flask-Migrate** for database version control.

## Features
- **Product Management:** Add, retrieve, and update product details.
- **Order Processing:** Validate stock and place orders.
- **Database Integration:** Uses **PostgreSQL** with SQLAlchemy ORM.
- **Migrations:** Managed using **Flask-Migrate**.
- **Docker Support:** Fully containerized for deployment.
- **RESTful API:** Built with JSON responses and proper error handling.

---

## Tech Stack
- **Backend:** Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-Marshmallow
- **Database:** PostgreSQL
- **Containerization:** Docker
- **Testing:** Pytest, Unittest

---

## Installation
### 1. Clone the Repository
```sh
$ git clone <repo_url>
$ cd flask-ecommerce-api
```

### 2. Create a Virtual Environment
```sh
$ python -m venv venv
$ source venv/bin/activate  # For Mac/Linux
$ venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 4. Setup Database (PostgreSQL)
Ensure **PostgreSQL** is installed and running. Update `app.config['SQLALCHEMY_DATABASE_URI']` in `config.py` with your PostgreSQL credentials.

Create the database:
```sh
$ psql -U postgres
postgres=# CREATE DATABASE ecommerce_db;
postgres=# \q
```

### 5. Run Database Migrations
```sh
$ flask db init       # Initialize migration folder (only once)
$ flask db migrate    # Generate migration scripts
$ flask db upgrade    # Apply migrations
```

---

## Running the Application
### 1. Start the Flask Server
```sh
$ flask run
```
The API will be available at: **http://127.0.0.1:5000/**

### 2. Running with Docker
Build and run the application in a **Docker container**:
```sh
# Build Docker Image
$ docker build -t flask-ecommerce . 
#Run Container
$ docker run -p 5000:5000 flask-ecommerce
# Run with Docker Compose
$ docker-compose up --build

```

---

## API Endpoints
### 1. Product Endpoints
| Method | Endpoint       | Description            |
|--------|--------------|------------------------|
| GET    | /products    | Fetch all products     |
| POST   | /products    | Add a new product      |

**POST /products Request Body:**
```json
{
  "name": "Laptop",
  "description": "High-end gaming laptop",
  "price": 1500.99,
  "stock": 10
}
```

### 2. Order Endpoints
| Method | Endpoint    | Description         |
|--------|------------|---------------------|
| POST   | /orders    | Place a new order   |

**POST /orders Request Body:**
```json
{
  "products": [
    {"product_id": 1, "quantity": 2},
    {"product_id": 3, "quantity": 1}
  ]
}
```

---

## Testing
Run tests using **pytest**:
```sh
$ pytest
```
Or using **Unittest**:
```sh
$ python -m unittest discover tests/
```

---

## Future Improvements
- Add authentication (JWT-based login/signup).
- Implement product categories.
- Enhance order tracking with timestamps.
- Deploy the API using **AWS/GCP/DigitalOcean**.

---



