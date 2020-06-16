from flask import Flask
from flask_cors import CORS
from config import env_config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# SQLAlchemy
dbsql = SQLAlchemy()
# PostgreSQL migration controller
migrate = Migrate()

def create_app(config_name):

    # Initiate the app
    app = Flask(__name__)

    # Enable Cross Origin requests
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

    # set config
    app.config.from_object(env_config[config_name])

    # initialize extensions
    dbsql.init_app(app)
    migrate.init_app(app, dbsql)

    from app.api import blueprint
    app.register_blueprint(blueprint, url_prefix='/v1')

    # Shell Context for the Flask Cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": dbsql}

    return app
