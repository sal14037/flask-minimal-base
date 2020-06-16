from flask import request, app
from flask_restx import Resource

from app.api.model.models import ModelDto
from app.api.model.service import ModelService

model_service = ModelService()

api = ModelDto.api
_model = ModelDto.model

@api.route('/')
@api.response(404, 'Model not found.')
class Model(Resource):

    @api.doc('Create a new model')
    @api.marshal_with(_model)
    @api.expect(_model)
    def post(self):
        """Create a new model"""
        model = model_service.create_model(api.payload)
        if not model:
            api.abort(404)
        else:
            return model

@api.route('/<int:id>')
@api.param('id', 'The model identifier')
@api.response(404, 'Model not found.')
class ModelWithID(Resource):
    @api.doc('Get model')
    @api.marshal_with(_model)
    def get(self, id):
        """Get a model given its identifier"""
        model = model_service.get_model_by_id(id)
        if not model:
            api.abort(404)
        else:
            return model

    @api.doc('Update model')
    @api.marshal_with(_model)
    @api.expect(_model)
    def put(self, id):
        """Update model given its identifier"""
        model = model_service.update_model_by_id(id,api.payload)
        if not model:
            api.abort(404)
        else:
            return model

    @api.doc('Delete model')
    @api.marshal_with(_model)
    def delete(self, id):
        """Delete model given its identifier"""
        model = model_service.delete_model_by_id(id)
        if model:
            api.abort(404)
        else:
            return "Success.",201


