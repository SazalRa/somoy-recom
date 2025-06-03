from flask import Flask, render_template
import os
from routes.routes import *

app = Flask(__name__)
app.template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
@app.route('/')
def home():
    return render_template('./index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/author-analysis')
def author_analysis():
    return render_template('author-analysis.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    print(f"Login attempt with email: {email}")

    if not email or not password:
        return jsonify({'error': 'Email and password required'}), 400

    user = get_user_by_email(email)
    if user and check_password_hash(user['password'], password):
        return jsonify({"success": True, 
                        "message": 'Login successful', 
                        "user_id": user['uuid']}), 200
        #return render_template('./dashboard.html')
    else:
        return jsonify({"success": False, "error": 'Invalid credentials'}), 401


if __name__ == '__main__':
    app.run(debug=True) 