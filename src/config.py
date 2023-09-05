import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ec9439cfc6c796ae2029594d'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'ec9439cfc6c796ae2029594d'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') \
                              or "postgresql://sales_db:sales_db@192.168.1.5:5432/sales_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.googlemail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or 1
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'skarandanis@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or '7ujm&UJM'
    ADMINS = ['skarandanis@gmail.com']

    LANGUAGES = ['en', 'gr']
    BABEL_DEFAULT_LOCALE = 'en'

    ELASTICSEARCH_SCHEME = os.environ.get('ELASTICSEARCH_SCHEME') or 'https://'
    ELASTICSEARCH_HOST = os.environ.get('ELASTICSEARCH_HOST') or 'api.elastic'
    ELASTICSEARCH_PORT = os.environ.get('ELASTICSEARCH_PORT') or 443
    ELASTICSEARCH_USERNAME = os.environ.get('ELASTICSEARCH_USERNAME') or 'elastic'
    ELASTICSEARCH_PASSWORD = os.environ.get('ELASTICSEARCH_PASSWORD') or '19633bNYvlFbDY77Hqx534xs'

    REDIS_SCHEME = os.environ.get('REDIS_SCHEME') or 'http://'
    REDIS_HOST = os.environ.get('REDIS_HOST') or '192.168.1.5'
    REDIS_PORT = os.environ.get('REDIS_PORT') or 6379
    REDIS_DATABASE = os.environ.get('REDIS_DATABASE') or 0
    REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD') or 'password'

    CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", "redis://192.168.1.5:6379/0")
    CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", "redis://192.168.1.5:6379/0")

