from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identify
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from db import db

import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'zeus'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identify)

api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')


if __name__ == "__main__":
    db.init_app(app)
    ENVIRONMENT_DEBUG = os.environ.get("DEBUG", False)
    app.run(host='0.0.0.0', port=5000, debug=ENVIRONMENT_DEBUG)
