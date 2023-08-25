from flask import Blueprint, app, request, jsonify
import validators
from flask_jwt_extended import create_refresh_token, create_access_token

from src.constants.http_status_codes import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_401_UNAUTHORIZED, HTTP_200_OK
from src.services import user_service

auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


@auth.post('/register')
def register():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    if len(password) < 6:
        return jsonify({'error': "Password is too short"}), HTTP_400_BAD_REQUEST

    if len(username) < 3:
        return jsonify({'error': "User is too short"}), HTTP_400_BAD_REQUEST

    if not validators.email(email):
        return jsonify({'error': "Email is not valid"}), HTTP_400_BAD_REQUEST

    user = user_service.create(username, email, password)

    return jsonify({
        'message': "User created",
        'user': {
            'username': user.username, "email": user.email
        }

    }), HTTP_201_CREATED


@auth.post('/login')
def login():
    username = request.json.get('username', '')
    password = request.json.get('password', '')

    attempted_user = user_service.find_by_username(username)
    if attempted_user and attempted_user.check_password_correction(password):
        refresh = create_refresh_token(identity=attempted_user.id)
        access = create_access_token(identity=attempted_user.id)

        return jsonify({
            'user': {
                'refresh': refresh,
                'access': access,
                'username': attempted_user.username,
                'email': attempted_user.email_address
            }

        }), HTTP_200_OK

    return jsonify({'error': 'Wrong credentials'}), HTTP_401_UNAUTHORIZED