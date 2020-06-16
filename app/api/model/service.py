import uuid
import json
from flask import jsonify, Response
from flask_restx import abort

from app.api.utils.helper import updateobj

from app.api.model.models import Model, ModelDto

from app import dbsql as db

_model_model = ModelDto.model

class ModelService(object):

    def foo(self, payload):
        return ""

    def get_model_by_id(self, id):
        model=Model.query.filter(Model.id==id).first()
        return model

    def get_caregivers(self):
        models=Model.query.all()
        return models

    def create_model(self, model):
        newModel = Model()
        updateobj(newModel, model)
        db.session.add(newModel)
        db.session.commit()
        return newModel

    def update_model_by_id(self, id, updatedModel):
        model=Model.query.filter(Model.id==id).first()
        updateobj(model, updatedModel)
        db.session.commit()
        return model

    def delete_model_by_id(self, id):
        model=Model.query.filter(Model.id==id).first()
        db.session.delete(model)
        db.session.commit()
