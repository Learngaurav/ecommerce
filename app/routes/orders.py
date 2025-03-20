import json
from flask import Blueprint, request, jsonify
from app import db
from app.models import Product, Order
from app.schemas import order_schema
from app.utils import handle_exception

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/", methods=["POST"])
def place_order():
    try:
        data = request.get_json()
        products_list = data.get("products")  # Expecting [{"product_id": 1, "quantity": 2}, ...]

        if not products_list:
            return handle_exception("Order must contain products", 400)

        total_price = 0
        updated_products = []

        # Start transaction
        with db.session.begin_nested():
            for item in products_list:
                product_id = item.get("product_id")
                quantity = item.get("quantity")

                if not product_id or not isinstance(quantity, int) or quantity <= 0:
                    return handle_exception("Each product must have a valid product_id and quantity > 0", 400)

                product = Product.query.get(product_id)

                if not product:
                    return handle_exception(f"Product with ID {product_id} not found", 404)

                if product.stock < quantity:
                    return handle_exception(f"Insufficient stock for {product.name}", 400)

                # Deduct stock and calculate total price
                product.stock -= quantity
                total_price += product.price * quantity
                updated_products.append({"product_id": product.id, "quantity": quantity})

        # Create the order
        new_order = Order(products=json.dumps(updated_products), total_price=total_price)
        db.session.add(new_order)
        db.session.commit()

        return jsonify({"message": "Order placed successfully", "order_id": new_order.id, "total_price": total_price}), 201

    except Exception as e:
        return handle_exception(str(e), 500)
