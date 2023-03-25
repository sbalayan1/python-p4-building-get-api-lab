from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'
    serialize_rules = ('-baked_goods.bakery','-baked_goods.bakery_id')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    baked_goods = db.relationship('BakedGood', backref='bakery')
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'
    serialize_rules=('-bakery.baked_goods', '-bakery_id') #this basically says when you display the bakery, don't display the baked_goods property of that bakery

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    