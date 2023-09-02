import datetime
import logging
import os

from logging.handlers import RotatingFileHandler


from elasticsearch import Elasticsearch
from flask import Flask, request
from flask_babel import Babel
from flask_jwt_extended import JWTManager

from src.config import Config
from src.data_access import db, bcrypt
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

    elastic_url = created_app.config['ELASTICSEARCH_SCHEME'] + \
                  created_app.config['ELASTICSEARCH_HOST'] + ':' + str(created_app.config['ELASTICSEARCH_PORT'])

    elastic_username = created_app.config['ELASTICSEARCH_USERNAME']
    elastic_password = created_app.config['ELASTICSEARCH_PASSWORD']

    created_app.elasticsearch = Elasticsearch(elastic_url, basic_auth=(elastic_username, elastic_password))

    from src.error_routes import errors
    created_app.register_blueprint(errors)

    from src.auth_routes import auth
    created_app.register_blueprint(auth)

    from src.product_routes import products
    created_app.register_blueprint(products)

    from src.cart_routes import carts
    created_app.register_blueprint(carts)

    from src.order_routes import orders
    created_app.register_blueprint(orders)


    def get_locale():
        return request.accept_languages.best_match(created_app.config['LANGUAGES'])

    babel = Babel(created_app, locale_selector=get_locale)

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
