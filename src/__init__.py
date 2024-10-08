import datetime
import logging
import os

from logging.handlers import RotatingFileHandler

from elasticsearch import Elasticsearch
from flask import Flask, request
from flask_babel import Babel
from flask_celeryext import FlaskCeleryExt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

from src.celery import make_celery
from src.config import Config
from src.data_access import db, bcrypt
from src.services import mail

ext_celery = FlaskCeleryExt(create_celery_app=make_celery)

db_migration = Migrate()

ma = Marshmallow()


def create_app(test_config=None):
    created_app = Flask(__name__, instance_relative_config=True)
    logging.basicConfig(format='[%(asctime)s] %(levelname)s %(name)s: %(message)s')
    logging.getLogger().setLevel(logging.DEBUG)
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

    if test_config is None:
        created_app.config.from_object(Config)
    else:
        created_app.config.from_mapping(test_config)

    initialize_extensions(created_app)
    
    created_app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(minutes=90)
    created_app.config['JWT_REFRESH_TOKEN_EXPIRES'] = datetime.timedelta(minutes=90)

    elastic_url = created_app.config['ELASTICSEARCH_SCHEME'] + \
                  created_app.config['ELASTICSEARCH_HOST'] + ':' + str(created_app.config['ELASTICSEARCH_PORT'])

    elastic_username = created_app.config['ELASTICSEARCH_USERNAME']
    elastic_password = created_app.config['ELASTICSEARCH_PASSWORD']

    created_app.elasticsearch = Elasticsearch(
        elastic_url, basic_auth=(elastic_username, elastic_password), verify_certs=False)

    register_blueprint(created_app)

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


def initialize_extensions(app):
    db.init_app(app)
    db_migration.init_app(app, db)
    bcrypt.init_app(app)
    mail.init_app(app)
    JWTManager(app)
    ext_celery.init_app(app)
    ma.init_app(app)


def register_blueprint(app):
    from src.error_routes import errors
    app.register_blueprint(errors)

    from src.auth_routes import auth
    app.register_blueprint(auth)

    from src.product_routes import products
    app.register_blueprint(products)

    from src.cart_routes import carts
    app.register_blueprint(carts)

    from src.order_routes import orders
    app.register_blueprint(orders)
