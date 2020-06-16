import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Config:
    """Base configuration"""
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    TESTING = False
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'random_secret_key')  # used for hashing
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Development configuration"""
    ENV = 'development'
    DEBUG = True
    TESTING = True
    # Cognito configurations
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL')

class TestingConfig(Config):
    """Testing configuration"""
    FLASK_ENV = 'testing'
    TESTING = True
    DEBUG = False

class ProductionConfig(Config):
    """Production configuration"""
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL')
    pass

env_config = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
