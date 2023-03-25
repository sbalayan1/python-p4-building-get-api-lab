#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    res = [b.to_dict() for b in Bakery.query.all()]
    # for b in Bakery.query.all():
        # res.append(b.to_dict())
    return make_response(res, 200, {"content-type": "application/json"})

@app.route('/bakeries/<int:id>')
def bakery(id):
    res = Bakery.query.filter(Bakery.id == id).first().to_dict()
    return make_response(res, 200, {"content-type": "application/json"})

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    res = [b.to_dict() for b in BakedGood.query.order_by(BakedGood.price.desc()).all()]
    return make_response(res, 200, {"content-type":"application/json"})

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    res = BakedGood.query.order_by(BakedGood.price.desc()).first().to_dict()
    return make_response(res, 200, {"content-type":"application/json"})

if __name__ == '__main__':
    app.run(port=5555, debug=True)
    print('hello world')
