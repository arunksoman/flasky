from flask import Blueprint, request
from .models import User
from uuid import uuid4

user_bp = Blueprint("user", __name__, url_prefix="/api/v1/user")


@user_bp.post("/register")
def user_bp_():
    json_data = request.get_json()
    username = json_data["username"]
    password = json_data["password"]
    email = json_data["email"]
    u_id = str(uuid4())
    user = User(u_id=u_id, username=username, password=password, email=email)
    user.upsert()
    return {"msg": "Registration Successful"}, 200
