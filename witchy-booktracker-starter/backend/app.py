
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from models import init_db, User, UserBook
from recommendations import get_recommendations
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "dev-secret")
CORS(app)
db = init_db(app)

@app.route("/")
def home():
    return jsonify({"msg": "Witchy Booktracker backend alive"})

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    if User.get_by_email(data["email"]):
        return jsonify({"msg": "Email already exists"}), 400
    user = User.create(email=data["email"], password=data["password"])
    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token})

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.authenticate(data["email"], data["password"])
    if not user:
        return jsonify({"msg": "Bad credentials"}), 401
    token = create_access_token(identity=user.id)
    return jsonify({"access_token": token})

@app.route("/user/books", methods=["GET", "POST"])
@jwt_required()
def user_books():
    user_id = get_jwt_identity()
    if request.method == "POST":
        payload = request.json  # expects { "google_book_id": "...", "status": "read" }
        ub = UserBook.add_or_update(user_id, payload["google_book_id"], payload.get("status", "read"))
        return jsonify({"msg": "saved"})
    else:
        books = UserBook.list_for_user(user_id)
        return jsonify([b.to_dict() for b in books])

@app.route("/recommendations", methods=["GET"])
@jwt_required()
def recommendations():
    user_id = get_jwt_identity()
    recs = get_recommendations(user_id)
    return jsonify(recs)

if __name__ == "__main__":
    app.run(debug=True)
