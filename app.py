import os
from networkx import Graph
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from resources.navigation import GetMe
from scripts.json_loader import load_graph_to_memory
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.secret_key = 'superKEYsuperSECRETWHATOUT'
api = Api(app)

api.add_resource(GetMe, '/GetMe')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    graph = load_graph_to_memory('map.json')
    app.run(port=5000, debug=True)
