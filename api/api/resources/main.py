"""Entrypoint of the main API Resources."""
# Flask based imports
from flask_restplus import Resource, Namespace
from app import db
from models import *

# Empty name is required to have the desired url path
api = Namespace(name='', description='Main API namespace.')


@api.route('/hello/<name>')
@api.doc(params={'name': 'The name of the person to return hello.'})
class HelloWorld(Resource):
    """HelloWorld resource class."""

    def get(self, name):
        """Get method."""
        return {'hello': name}

@api.route('/risk/<int:rid>')
@api.route('/risk')
@api.doc(params={'name': 'The name of the person to return hello.'})
class Risk(Resource):
    """ """
    def get(self, rid=0):
        if (rid is not 0):
            risk = RiskType.query.filter_by(id=rid).first()
            return risk.to_json()
        else:
            risks = RiskType.query.all()
            return [x.to_json() for x in risks]
    
    def post(self):
        pass

    def put(self):
        pass