# RESTFul API with Python/Flask

This project implements a RESTful API in Python using Flask.

## Features

- Fetches initial product data from the [Dummy JSON API](https://dummyjson.com/products).
- Allows CRUD operations on the fetched data.

## Endpoints

- `GET /get-products`: Retrieve all products.
- `POST /add-product`: Add a new product (validation included).
- `PUT /update-proiduct/<product_id>`: Update an existing product.
- `DELETE /delete-proiduct/<product_id>`: Delete a product.

## Setup

1. Clone the repository.
2. Create a virtual environment and install the required dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Use venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```
