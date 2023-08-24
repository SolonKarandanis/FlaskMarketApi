from flask import Blueprint, app, request

auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


@auth.post('/register')
def register():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
