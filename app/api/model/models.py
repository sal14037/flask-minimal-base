from flask_restx import Namespace, fields

from app import dbsql as db

class Model(db.Model):
    __tablename__ = "models"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<Test %r>' % self.name

class ModelDto:
    api = Namespace('Model', description='Model related operations')

    model = api.model('model', {
        'id': fields.String(description='test Identifier'),
        'name': fields.String()
    })

    @staticmethod
    def convert_model_json(model):
        pass
