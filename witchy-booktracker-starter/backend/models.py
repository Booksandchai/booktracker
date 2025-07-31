
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

db = SQLAlchemy()

def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///local.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password_hash = db.Column(db.String(255))

    @classmethod
    def create(cls, email, password):
        user = cls(email=email, password_hash=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def authenticate(cls, email, password):
        user = cls.get_by_email(email)
        if user and check_password_hash(user.password_hash, password):
            return user
        return None

class UserBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    google_book_id = db.Column(db.String(255))
    status = db.Column(db.String(50))  # e.g., "read", "reading", "wishlist"

    @classmethod
    def add_or_update(cls, user_id, google_book_id, status):
        ub = cls.query.filter_by(user_id=user_id, google_book_id=google_book_id).first()
        if ub:
            ub.status = status
        else:
            ub = cls(user_id=user_id, google_book_id=google_book_id, status=status)
            db.session.add(ub)
        db.session.commit()
        return ub

    @classmethod
    def list_for_user(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()

    def to_dict(self):
        return {
            "google_book_id": self.google_book_id,
            "status": self.status,
        }
