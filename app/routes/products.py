from flask import Blueprint, request, jsonify
from app import db
from app.models import Product
from app.schemas import product_schema, products_schema
from app.utils import handle_exception

products_bp = Blueprint("products", __name__)

@products_bp.route("/", methods=["GET"])
def get_products():
    try:
        products = Product.query.all()
        return jsonify(products_schema.dump(products))
    except Exception as e:
        return handle_exception(str(e), 500)

@products_bp.route("/", methods=["POST"])
def add_product():
    try:
        data = request.json
        if not all(k in data for k in ("name", "price", "stock")):
            return handle_exception("Missing required fields", 400)

        new_product = Product(
            name=data["name"],
            description=data.get("description", ""),
            price=float(data["price"]),
            stock=int(data["stock"])
        )
        db.session.add(new_product)
        db.session.commit()
        return product_schema.jsonify(new_product), 201
    except ValueError:
        return handle_exception("Invalid data type for price or stock", 400)
    except Exception as e:
        return handle_exception(str(e), 500)
