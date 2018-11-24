import os
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqllite:///data.db')
app.secret_key = 'superKEYsuperSECRETWHATOUT'
api = Api(app)

class Index(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('message',
                        type=str,
                        help='say hi to heroku'
                        )
    def get(self):
        return {"message": "Hello world"}

    def post(self):
        data = Index.parser.parse_args()
        print('***********{}********'.format(data['message']))





api.add_resource(Index, '/')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
