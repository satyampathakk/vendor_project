# vendor_project
                                        # Dependency
# Django Project Setup Guide

## 1. Install Django and Django rest framework

```bash
pip install django
pip install django restframework
```
## 2. Install Postgres Sql 
 ```bash
 pip install psycopg2
 ```

## 3. Configure settings.py in vendor_project folder 
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
## 4. install jwt
```bash 
pip install djangorestframework_simplejwt
```
## Other command
```bash
python manage.py makemigrations
python manage.py migrate # to change schema in the database
python manage.py runserver # to start the django server
python manage.py flush #to clear the database all the data 
```
#  Endpoint and explaination of using them 

## Token Obtain Endpoint

- **URL:** `/api/token/<str:vendor_code>/`
- **Method:** GET
- **Description:** This endpoint is used to obtain a JWT token for authentication. It takes a `vendor_code` as a path parameter and returns a JWT token if the vendor with the provided vendor code exists.
- **Parameters:**
  - `vendor_code` (path parameter): The unique code identifying the vendor.
- **Response:**
  - `access` (string): JWT access token.
  - `refresh` (string): JWT refresh token.
  - `vendor_id` (integer): ID of the vendor associated with the token.

## Vendor List Endpoint

- **URL:** `/api/vendors/`
- **Method:** GET, POST
- **Description:** This endpoint is used to retrieve a list of all vendors or create a new vendor.
- **Parameters:** None for GET request. Request body should contain vendor data for POST request.
- **Response:** JSON array containing vendor objects for GET request. Newly created vendor object for POST request.

## Vendor Detail Endpoint

- **URL:** `/api/vendors/<int:pk>/`
- **Method:** GET, PUT, DELETE
- **Description:** This endpoint is used to retrieve, update, or delete a specific vendor by its ID (`pk`).
- **Parameters:**
  - `pk` (path parameter): ID of the vendor.
- **Response:** JSON object containing the vendor details.

## Purchase Order List Endpoint

- **URL:** `/api/purchase_orders/`
- **Method:** GET, POST
- **Description:** This endpoint is used to retrieve a list of all purchase orders or create a new purchase order.
- **Parameters:** None for GET request. Request body should contain purchase order data for POST request.
- **Response:** JSON array containing purchase order objects for GET request. Newly created purchase order object for POST request.

## Purchase Order Detail Endpoint

- **URL:** `/api/purchase_orders/<int:pk>/`
- **Method:** GET, PUT, DELETE
- **Description:** This endpoint is used to retrieve, update, or delete a specific purchase order by its ID (`pk`).
- **Parameters:**
  - `pk` (path parameter): ID of the purchase order.
- **Response:** JSON object containing the purchase order details.

## Vendor Performance Endpoint

- **URL:** `/api/vendors/<int:vendor_id>/performance/`
- **Method:** GET
- **Description:** This endpoint is used to retrieve the performance metrics of a specific vendor by its ID (`vendor_id`).
- **Parameters:**
  - `vendor_id` (path parameter): ID of the vendor.
- **Response:** JSON object containing the performance metrics of the vendor.

## Acknowledge Purchase Order Endpoint

- **URL:** `/api/purchase_orders/<int:po_id>/acknowledge/`
- **Method:** POST
- **Description:** This endpoint is used to acknowledge a purchase order by its ID (`po_id`). It updates the acknowledgment date of the purchase order and calculates the vendor's performance metrics.
- **Parameters:**
  - `po_id` (path parameter): ID of the purchase order.
- **Response:** Empty response with status code 204 (No Content) if successful.
