import json
from app.models import Product, db

def test_create_product(client):
    """Test adding a product successfully"""
    response = client.post("/products/", json={
        "name": "Laptop",
        "description": "Gaming Laptop",
        "price": 999.99,
        "stock": 10
    })
    data = response.get_json()
    
    assert response.status_code == 201
    assert data["name"] == "Laptop"
    assert data["price"] == 999.99

def test_create_product_missing_fields(client):
    """Test adding a product with missing fields"""
    response = client.post("/products/", json={"name": "Laptop"})
    data = response.get_json()

    assert response.status_code == 400
    assert "error" in data

def test_get_products(client):
    """Test fetching all products"""
    # Add a product first
    product = Product(name="Phone", description="Smartphone", price=500.0, stock=5)
    db.session.add(product)
    db.session.commit()

    response = client.get("/products/")
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) > 0
    assert data[0]["name"] == "Phone"
