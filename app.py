from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Sample product data - in a real application, this would come from a database
PRODUCTS = [
    {
        "id": 1,
        "name": "CASIO EXILIM EX-ZS6",
        "brand": "Casio",
        "price": 1500000,
        "description": "Compact digital camera with excellent image quality and easy-to-use features.",
        "image": "static/img/kamera8.jpg",
        "category": "Casio",
        "featured": True,
        "badge": "POPULAR"
    },
    {
        "id": 2,
        "name": "CANON POWERSHOT A2500",
        "brand": "Canon",
        "price": 1100000,
        "description": "Affordable Canon camera with great features for beginners and enthusiasts.",
        "image": "static/img/kamera1.jpg",
        "category": "Canon",
        "featured": True,
        "badge": "BEST SELLER"
    },
    {
        "id": 3,
        "name": "CANON IXY 10S",
        "brand": "Canon",
        "price": 2100000,
        "description": "Canon's stylish IXY series with advanced features and premium build.",
        "image": "static/img/kamera5.jpg",
        "category": "Canon",
        "featured": True,
        "badge": "PREMIUM"
    },
    {
        "id": 4,
        "name": "CANON POWERSHOT A400",
        "brand": "Canon",
        "price": 1550000,
        "description": "Reliable Canon camera with excellent image quality and manual controls.",
        "image": "static/img/kamera6.jpg",
        "category": "Canon",
        "featured": True,
        "badge": "AFFORDABLE"
    },
    {
        "id": 5,
        "name": "SONY CYBERSHOT DSC W620",
        "brand": "Sony",
        "price": 1200000,
        "description": "Sony's reliable Cyber-shot series with excellent zoom capabilities.",
        "image": "static/img/kamera3.jpg",
        "category": "Sony",
        "featured": False,
        "badge": ""
    },
    {
        "id": 6,
        "name": "NIKON COOLPIX S3500",
        "brand": "Nikon",
        "price": 1850000,
        "description": "Nikon's premium compact camera with exceptional image quality.",
        "image": "static/img/kamera4.jpg",
        "category": "Nikon",
        "featured": False,
        "badge": ""
    },
    {
        "id": 7,
        "name": "CASIO EXILIM EX-Z33",
        "brand": "Casio",
        "price": 1600000,
        "description": "Sleek and stylish digital camera with great performance for everyday use.",
        "image": "static/img/kamera7.jpg",
        "category": "Casio",
        "featured": False,
        "badge": ""
    },
    {
        "id": 8,
        "name": "BENQ AE120",
        "brand": "BenQ",
        "price": 1200000,
        "description": "Unique BenQ camera with distinctive design and solid performance.",
        "image": "static/img/kamera2.jpg",
        "category": "BenQ",
        "featured": False,
        "badge": ""
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/api/products')
def get_all_products():
    """Get all products"""
    return jsonify(PRODUCTS)

@app.route('/api/products/<int:product_id>')
def get_product(product_id):
    """Get a specific product by ID"""
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404

@app.route('/api/products/category/<category>')
def get_products_by_category(category):
    """Get products by category"""
    category_products = [p for p in PRODUCTS if p["category"].lower() == category.lower()]
    return jsonify(category_products)

@app.route('/api/products/featured')
def get_featured_products():
    """Get featured products"""
    featured_products = [p for p in PRODUCTS if p["featured"]]
    return jsonify(featured_products)

@app.route('/api/categories')
def get_categories():
    """Get all unique categories"""
    categories = list(set([p["category"] for p in PRODUCTS]))
    return jsonify(sorted(categories))

@app.route('/api/products/search', methods=['GET'])
def search_products():
    """Search products by name or brand"""
    query = request.args.get('q', '').lower()
    if query:
        results = [p for p in PRODUCTS if query in p["name"].lower() or query in p["brand"].lower()]
        return jsonify(results)
    else:
        return jsonify(PRODUCTS)

if __name__ == '__main__':
    app.run(debug=True, port=1919)