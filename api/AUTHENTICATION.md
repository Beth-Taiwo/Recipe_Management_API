# Authentication Setup

This API uses token-based authentication to secure its endpoints. Here is how to set up and test the authentication.

## User Registration

**Endpoint:** `POST /api/signup`

**Request Parameters:**

- Body:

  ```json
  {
    "username": "string",
    "email": "string",
    "password": "string"
  }
  ```

  **Response:**

- Status: `201 Created`
- Body:
  ```json
  {
    "token": "string"
  }
  ```

## User Login

**Endpoint:** `POST /api/login`

**Request Parameters:**

- Body:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```

**Response:**

- Status: `200 OK`
- Body:
  ```json
  {
    "user": {
      "token": "string",
      "id": "number",
      "username": "string",
      "password": "string"
    }
  }
  ```
