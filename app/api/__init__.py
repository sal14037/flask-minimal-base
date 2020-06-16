from flask_restx import Api
from os import getenv
from flask import Blueprint

from app.api.model.routes import api as model_ns

blueprint = Blueprint('api', __name__)
# Disable Swagger UI on production environment
swagger_enabled = False if (getenv('APP_ENV') == 'prod') else '/'

api = Api(blueprint,
          doc=swagger_enabled,  # set to False to disable
          title='RESTful API',
          version='1.0',
          description='RESTful API'
          )

api.add_namespace(model_ns, path='/model')

@api.errorhandler(Exception)
def handle_error(e):
    code = 500
    if hasattr(e, 'code'):
        code = e.code
    return {'message': str(e)}, code
