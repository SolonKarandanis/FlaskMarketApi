import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ec9439cfc6c796ae2029594d'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'ec9439cfc6c796ae2029594d'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') \
                              or "postgresql://sales_db:sales_db@192.168.1.5:5432/sales_db"