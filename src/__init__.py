import datetime
import logging
import os

from logging.handlers import RotatingFileHandler

from flask import Flask, request
from flask_jwt_extended import JWTManager

from src.cart_routes import carts
from src.config import Config
from src.data_access import db, bcrypt
from src.product_routes import products
from src.services import mail


def create_app(test_config=None):
    created_app = Flask(__name__, instance_relative_config=True)
    logging.basicConfig(format='[%(asctime)s] %(levelname)s %(name)s: %(message)s')
    logging.getLogger().setLevel(logging.DEBUG)
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

    if test_config is None:
        created_app.config.from_object(Config)
    else:
        created_app.config.from_mapping(test_config)

    db.init_app(created_app)
    bcrypt.init_app(created_app)
    mail.init_app(created_app)
    created_app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(minutes=30)
    created_app.config['JWT_REFRESH_EXPIRATION_DELTA'] = datetime.timedelta(minutes=30)
    JWTManager(created_app)

    from src.auth_routes import auth
    created_app.register_blueprint(auth)
    created_app.register_blueprint(products)
    created_app.register_blueprint(carts)

    if not created_app.debug:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/flask_market.log', maxBytes=10240,
                                           backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        created_app.logger.addHandler(file_handler)

        created_app.logger.setLevel(logging.INFO)
        created_app.logger.info('FlaskMarket startup')

    return created_app
