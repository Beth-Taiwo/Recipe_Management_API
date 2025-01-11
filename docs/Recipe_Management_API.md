**File: /Users/beth/Documents/Recipe_Management_API/docs/Recipe_Management_API.md**

````markdown
# Recipe Management API

## Description

This API provides functionality for managing recipes, users, and related operations.

## Endpoints

### 1. Create User

- **Method:** POST
- **URL:** `http://127.0.0.1:8000/api/signup`
- **Body:**
  ```json
  {
    "username": "beth",
    "email": "Beth@gmail.com",
    "password": "**********"
  }
  ```
````

- **Response:**
  - Status Code: 201 Created
  - Body:
    ```json
    {
      "user": {
        "id": 1,
        "username": "beth",
        "email": "Beth@gmail.com",
        "password": "**********"
      },
      "token": "****************************************"
    }
    ```
- **Possible Status Codes:**
  - 201: User created successfully
  - 400: Bad request (e.g., invalid data)
  - 409: Conflict (e.g., username already exists)

### 2. User Login

- **Method:** POST
- **URL:** `http://127.0.0.1:8000/api/login`
- **Body:**
  ```json
  {
    "username": "beth",
    "password": "**********"
  }
  ```
- **Response:**
  - Status Code: 200 OK
  - Body:
    ```json
    {
      "user": {
        "id": 1,
        "username": "beth",
        "email": "Beth@gmail.com",
        "password": "**********"
      },
      "token": "****************************************"
    }
    ```
- **Possible Status Codes:**
  - 200: Login successful
  - 400: Bad request (e.g., missing fields)
  - 401: Unauthorized (incorrect credentials)

### 3. Retrieve Users

- **Method:** GET
- **URL:** `http://127.0.0.1:8000/api/users`
- **Response:**
  - Status Code: 200 OK
  - Body:
    ```json
    [
      {
        "id": 1,
        "username": "beth",
        "email": "Beth@gmail.com"
      }
      // ... more users
    ]
    ```
- **Possible Status Codes:**
  - 200: Success
  - 401: Unauthorized (if authentication is required)

### 4. Retrieve User by ID

- **Method:** GET
- **URL:** `http://127.0.0.1:8000/api/users/{id}`
- **Response:**
  - Status Code: 200 OK
  - Body:
    ```json
    {
      "id": 2,
      "username": "john_doe",
      "email": "john@example.com"
    }
    ```
- **Possible Status Codes:**
  - 200: Success
  - 404: User not found

### 5. Retrieve Recipes

- **Method:** GET
- **URL:** `http://127.0.0.1:8000/api/recipes`
- **Headers:**
  - Authorization: Token {your_token_here}
- **Response:**

  - Status Code: 200 OK
  - Body:

    ```json
    {
      "count": 2,
      "next": "https://bethtaiwo23.pythonanywhere.com/api/recipes/?page=2",
      "previous": null,
      "results": [
        {
          "id": 1,
          "ingredients": [
            {
              "id": 1,
              "name": "Eggs"
            }
          ],
          "category": "Breakfast",
          "course": null,
          "title": "Bread & Fried Egg",
          "description": "just a quick and simple breakfast",
          "instructions": "1. Heat oil in pan\r\n2. Crake egg in bowl and add a pinch of salt\r\n3. Whisk egg and pour in pan\r\n4. Flig egg to the opposite side\r\n5. Serve with bread and any beverage of your choice",
          "preparation_time": 2,
          "cooking_time": 4,
          "servings": 1,
          "created_date": "2025-01-11T13:20:41.650335Z",
          "created_by": 1
        }
        // ... more recipes
      ]
    }
    ```

- **Possible Status Codes:**
  - 200: Success
  - 401: Unauthorized

### 6. Filter Recipe by Category

- **Method:** GET
- **URL:** `http://127.0.0.1:8000/api/recipescategory/{category_name}`
- **Headers:**
  - Authorization: Token {your_token_here}
- **Response:**
  - Status Code: 200 OK
  - Body:
    ```json
    [
      {
        "id": 2,
        "title": "Caesar Salad",
        "category": "Salad",
        "ingredients": ["lettuce", "croutons", "parmesan", "caesar dressing"],
        "instructions": "..."
      }
      // ... more recipes in the category
    ]
    ```
- **Possible Status Codes:**
  - 200: Success
  - 401: Unauthorized
  - 404: No recipes found in the category

### 7. Filter Recipe by Ingredient

- **Method:** GET
- **URL:** `http://127.0.0.1:8000/api/recipes/ingredient/{ingredient_name}`
- **Headers:**
  - Authorization: Token {your_token_here}
- **Response:**
  - Status Code: 200 OK
  - Body:
    ```json
    [
      {
        "id": 3,
        "title": "Suya Chicken",
        "ingredients": ["chicken", "Suya spice", "onions", "peppers"],
        "instructions": "..."
      }
      // ... more recipes with the ingredient
    ]
    ```
- **Possible Status Codes:**
  - 200: Success
  - 401: Unauthorized
  - 404: No recipes found with the ingredient

### 8. Get Recipes per Page

- **Method:** GET
- **URL:** `http://127.0.0.1:8000/api/recipes/?page={page_number}`
- **Headers:**
  - Authorization: Token {your_token_here}
- **Response:**
  - Status Code: 200 OK
  - Body:
    ```json
    {
      "count": 50,
      "next": "http://127.0.0.1:8000/api/recipes/?page=3",
      "previous": "http://127.0.0.1:8000/api/recipes/?page=1",
      "results": [
        {
          "id": 11,
          "title": "Grilled Salmon",
          "ingredients": ["salmon", "lemon", "dill", "olive oil"],
          "instructions": "..."
        }
        // ... more recipes (typically 10 per page)
      ]
    }
    ```
- **Possible Status Codes:**
  - 200: Success
  - 401: Unauthorized
  - 404: Page not found

### 9. Update Recipe by ID

- **Method:** PUT
- **URL:** `http://127.0.0.1:8000/api/recipes/{id}`
- **Headers:**
  - Authorization: Token {your_token_here}
- **Body:**
  ```json
  {
    "title": "Updated Recipe Title",
    "ingredients": ["ingredient1", "ingredient2"],
    "instructions": "Updated instructions..."
  }
  ```
- **Response:**
  - Status Code: 200 OK
  - Body:
    ```json
    {
      "id": 1,
      "title": "Updated Recipe Title",
      "ingredients": ["ingredient1", "ingredient2"],
      "instructions": "Updated instructions..."
    }
    ```
- **Possible Status Codes:**
  - 200: Success
  - 400: Bad Request (invalid data)
  - 401: Unauthorized
  - 404: Recipe not found

### 10. Delete Recipe by ID

- **Method:** DELETE
- **URL:** `http://127.0.0.1:8000/api/recipes/{id}`
- **Headers:**
  - Authorization: Token {your_token_here}
- **Response:**
  - Status Code: 204 No Content
- **Possible Status Codes:**
  - 204: Success (Recipe deleted)
  - 401: Unauthorized
  - 404: Recipe not found

### 11. Update User Information

- **Method:** PATCH
- **URL:** `http://127.0.0.1:8000/api/user/{id}`
- **Body:**
  ```json
  {
    "username": "Beth",
    "email": "popoola.taiwo22@gmail.com",
    "password": "**********"
  }
  ```
- **Response:**
  - Status Code: 200 OK
  - Body:
    ```json
    {
      "id": 1,
      "username": "Beth",
      "email": "popoola.taiwo22@gmail.com"
    }
    ```
- **Possible Status Codes:**
  - 200: Success
  - 400: Bad Request (invalid data)
  - 401: Unauthorized
  - 404: User not found

## General Notes

- All endpoints that require authentication should include the Authorization header with a valid token.
- Requests with invalid data will typically return a 400 Bad Request status with details about the error.
- Unauthorized access attempts will return a 401 Unauthorized status.
- For endpoints that involve specific resources (like a user or recipe by ID), a 404 Not Found status will be returned if the resource doesn't exist.
