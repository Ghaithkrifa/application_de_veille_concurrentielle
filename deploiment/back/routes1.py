from flask import Blueprint
from controllers1 import createUser, getUsers,login, deleteUser, getUser, updateUser,sentMail
from flask_jwt_extended import jwt_required
user_bp1 = Blueprint("home_bp1", __name__)
user_bp1.route("/create", methods=["POST"])(createUser)
user_bp1.route("/users", methods=["GET"])(getUsers)
user_bp1.route("/login", methods=["POST"])(login)
user_bp1.route("/delete/<email>", methods=["DELETE"])(deleteUser)
user_bp1.route("/users/<email>", methods=["GET"])(getUser)
user_bp1.route("/update/<oldEmail>", methods=["PUT"])(updateUser) 
user_bp1.route("/send", methods=["POST"])(sentMail) 
