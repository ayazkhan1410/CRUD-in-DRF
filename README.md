
# Django REST Framework: CRUD Operations with Token Authentication

This project demonstrates how to implement CRUD (Create, Read, Update, Delete) operations with Django REST Framework (DRF) using token-based authentication. The project includes user login, transaction management, and secure access control using tokens.

## Features

- **CRUD Operations**: Manage transactions with endpoints to create, retrieve, update, and delete records.
- **Token Authentication**: Secure access to API endpoints using token-based authentication.
- **User Login**: Obtain authentication tokens by validating user credentials.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ayazkhan1410/CRUD-in-DRF.git
   cd your-repo-name
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### 1. Get All Transactions

- **URL**: `/api/transactions/`
- **Method**: `GET`
- **Response**: List of all transactions.

### 2. Create a Transaction

- **URL**: `/api/transactions/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "field1": "value1",
    "field2": "value2"
  }
  ```
- **Response**: Transaction creation confirmation.

### 3. Update a Transaction (Partial Update)

- **URL**: `/api/transactions/`
- **Method**: `PATCH`
- **Request Body**:
  ```json
  {
    "id": "transaction_id",
    "field_to_update": "new_value"
  }
  ```
- **Response**: Partial update confirmation.

### 4. Update a Transaction (Full Update)

- **URL**: `/api/transactions/`
- **Method**: `PUT`
- **Request Body**:
  ```json
  {
    "id": "transaction_id",
    "field1": "new_value1",
    "field2": "new_value2"
  }
  ```
- **Response**: Full update confirmation.

### 5. Delete a Transaction

- **URL**: `/api/transactions/`
- **Method**: `DELETE`
- **Request Body**:
  ```json
  {
    "id": "transaction_id"
  }
  ```
- **Response**: Deletion confirmation.

### 6. User Login

- **URL**: `/api/login/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
- **Response**: Authentication token if credentials are valid.

## Authentication

This project uses **Token Authentication** to secure API endpoints. To access the protected endpoints, include the token in the `Authorization` header of your requests:

```http
Authorization: Token <your_token>
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

For any questions or issues, feel free to reach out.

---

Feel free to adjust the README as necessary to better match your project's specifics.
```
