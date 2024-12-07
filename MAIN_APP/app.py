from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def get_data():
    try:
        response = requests.get("https://dummyjson.com/products", timeout=10)
        response.raise_for_status()
        return response.json().get("products", [])
    except requests.exceptions.RequestException as e:
        print(f"error fetching products: {e}")
        return []


products = get_data()

@app.route("/get-products")
def get_all_products():
    return jsonify(products)


@app.route("/add-product", methods=["POST"])
def add_product():
    data = request.get_json()

    # validate the fields
    fields_required = ["title", "price", "category"]
    missing_fields = [field for field in fields_required if field not in data]

    if missing_fields:
        return jsonify({"error": f"missing fileds: {', '.join(missing_fields)}"}), 400
    
    # add the product if fields are valid
    # add id to the new product
    data["id"] = max(p["id"] for p in products) + 1
    # add this data to the products list
    products.append(data)
    return jsonify(products), 201

@app.route("/update-proiduct/<product_id>", methods=["PUT"])
def update_product(product_id):
    product_id = int(product_id)
    # find the product from the products
    product = next((p for p in products if p["id"] == product_id), None)
    # update the product details
    if product:
        updated_data = request.get_json()
        product.update(updated_data)
        return jsonify(products), 200
    return jsonify({"error": "product not found"}), 404

@app.route("/delete-product/<product_id>", methods=["DELETE"])
def delete_product(product_id):
    # just filter out the deleted product and update the list
    global products
    products = [p for p in products if p["id"] != product_id]
    return jsonify({"message": "product deleted succesfully", "products": products}), 200

app.run(debug=True)