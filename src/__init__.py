import logging
import os
from logging.handlers import RotatingFileHandler

from flask import Flask, request
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from src.auth import auth
from src.config import Config


def create_app(test_config=None):
    created_app = Flask(__name__, instance_relative_config=True)
    logging.basicConfig(format='[%(asctime)s] %(levelname)s %(name)s: %(message)s')
    logging.getLogger().setLevel(logging.DEBUG)
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

    if test_config is None:
        created_app.config.from_object(Config)
    else:
        created_app.config.from_mapping(test_config)

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


app = create_app()
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
mail = Mail(app)
app.register_blueprint(auth)
