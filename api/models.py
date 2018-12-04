from flask_sqlalchemy import SQLAlchemy
from app import db


# mixin to support json serialization
class OutputMixin(object):
    RELATIONSHIPS_TO_DICT = False

    def __iter__(self):
        return self.to_dict().iteritems()

    def to_dict(self, rel=None, backref=None):
        if rel is None:
            rel = self.RELATIONSHIPS_TO_DICT
        res = {column.key: getattr(self, attr)
               for attr, column in self.__mapper__.c.items()}
        if rel:
            for attr, relation in self.__mapper__.relationships.items():
                # Avoid recursive loop between to tables.
                if backref == relation.table:
                    continue
                value = getattr(self, attr)
                if value is None:
                    res[relation.key] = None
                elif isinstance(value.__class__, DeclarativeMeta):
                    res[relation.key] = value.to_dict(backref=self.__table__)
                else:
                    res[relation.key] = [i.to_dict(backref=self.__table__)
                                         for i in value]
        return res

    def to_json(self, rel=None):
        def extended_encoder(x):
            if isinstance(x, datetime):
                return str(x.isoformat())
            if isinstance(x, UUID):
                return str(x)
        if rel is None:
            rel = self.RELATIONSHIPS_TO_DICT
        return json.dumps(self.to_dict(rel), default=extended_encoder)

risk_type_values=db.Table(
    'risk_type_values',
    db.Column('risk_type_id', db.Integer, db.ForeignKey('risk_type.id'), primary_key=True),
    db.Column('field_id', db.Integer, db.ForeignKey('field.id'), primary_key=True)
)

class RiskType(OutputMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    fields = db.relationship('Field', secondary=risk_type_values, lazy='subquery',
        backref=db.backref('risktypes', lazy=True))
    models = db.relationship('RiskModel', backref='riskmodel', lazy=True)

class Field(OutputMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    generic_type_id = db.relationship('GenericType', backref='field', lazy=True)
    values = db.relationship('FieldValue', backref='field', lazy=True)

class GenericType(OutputMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    nullable = db.Column(db.Boolean, default=True) 
    field_id = db.Column(db.Integer, db.ForeignKey('field.id'),
        nullable=False)

class FieldValue(OutputMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Text, nullable=False)
    field_id = db.Column(db.Integer, db.ForeignKey('field.id'),
        nullable=False)   
    risk_model_id = db.Column(db.Integer, db.ForeignKey('risk_model.id'),
        nullable=False) 

class RiskModel(OutputMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    risk_type_id = db.Column(db.Integer, db.ForeignKey('risk_type.id'),
        nullable=False) 
    field_values = db.relationship('FieldValue', backref='riskmodel', lazy=True)     
         





