from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from model import get_user_by_email  # Replace with your actual DB function

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    print(f"Login attempt with email: {email}")

    if not email or not password:
        return jsonify({'error': 'Email and password required'}), 400

    user = get_user_by_email(email)
    if user and check_password_hash(user['password'], password):
        return jsonify({
            "success": True, 
            "message": 'Login successful', 
            "user_id": user['id']}), 200
    else:
        return jsonify({"success": False, "error": 'Invalid credentials'}), 401