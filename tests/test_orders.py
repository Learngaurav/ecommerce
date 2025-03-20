import json
from app.models import Product, db

def test_place_order_success(client):
    """Test successfully placing an order"""
    # Add a product to the DB
    product = Product(name="Tablet", description="Android Tablet", price=300.0, stock=10)
    db.session.add(product)
    db.session.commit()

    response = client.post("/orders/", json={
        "products": [{"product_id": product.id, "quantity": 2}]
    })
    data = response.get_json()

    assert response.status_code == 201
    assert "order_id" in data
    assert data["total_price"] == 600.0  # 2 * 300

def test_place_order_insufficient_stock(client):
    """Test ordering more than available stock"""
    product = Product(name="Headphones", description="Noise Cancelling", price=100.0, stock=2)
    db.session.add(product)
    db.session.commit()

    response = client.post("/orders/", json={
        "products": [{"product_id": product.id, "quantity": 5}]
    })
    data = response.get_json()

    assert response.status_code == 400
    assert "Insufficient stock" in data["error"]

def test_place_order_invalid_product(client):
    """Test ordering a product that doesn't exist"""
    response = client.post("/orders/", json={
        "products": [{"product_id": 999, "quantity": 1}]
    })
    data = response.get_json()

    assert response.status_code == 404
    assert "Product with ID 999 not found" in data["error"]
