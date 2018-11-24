import os
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from resources.navigation import GetMe

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.secret_key = 'superKEYsuperSECRETWHATOUT'
api = Api(app)



api.add_resource(GetMe, '/GetMe')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
