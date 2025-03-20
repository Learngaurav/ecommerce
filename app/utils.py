from flask import jsonify

def handle_exception(error_message, status_code=400):
    response = {"error": error_message}
    return jsonify(response), status_code
