from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from security import authenticate, identity

app = Flask(__name__)
# Turns off the FlaskSQLAlchemy tracker, not the SQLAlchemy tracker
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.secret_key = 'secret'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity) # jwt creates /auth endpoint

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items/')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores/')
api.add_resource(UserRegister, '/register/')

if __name__ == '__main__':
    # Putting import here prevents circular dependencies
    # models above will also use db
    from db import db
    db.init_app(app)
    app.run(port=8888, debug=True)
