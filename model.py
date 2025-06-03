from pymongo import MongoClient
import uuid
from werkzeug.security import generate_password_hash
client = MongoClient("mongodb://localhost:27017/")
db = client["somoy_recom"]
users = db["users"]

def create_user(email, password, name):
    user = {
        "uuid": str(uuid.uuid4()),
        "email": email,
        "password": generate_password_hash(password),  # Store hashed password in production!
        "name": name
    }
    users.insert_one(user)
    return user
def get_user_by_email(email):
    return users.find_one({"email": email})
#create_user("sazalrahman10@somoy.tv","sazal@321","Sazal Rahman")
# Example usage:
# new_user = create_user("test@example.com", "securepassword", "Somoy")