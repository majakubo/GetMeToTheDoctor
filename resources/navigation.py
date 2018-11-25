from flask_restful import Resource, reqparse


class GetMe(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('from',
                        type=dict,
                        required=True,
                        help='Send starting point qr/room_name')
    parser.add_argument('to',
                        type=dict,
                        required=True,
                        help='You need to type')

    def post(self):
        data = GetMe.parser.parse_args()
        if data:
            if data['from']['id'] == "sala 101" and data['to']['id'] == 'sala 106':
                return {"route":
                            [
                                {"direction": "prosto", "distance": "5", "hint": "kieruj się prosto w stronę sali 101"},
                                {"direction": "lekko w prawo", "distance": "2", "hint": "skręć lekko w prawo"},
                                {"direction": "prosto", "distance": "1", "hint": "kieruj się prosto w kierunku sal 102, 103"},
                                {"direction": "ostro w prawo", "distance": "2", "hint": "skręć ostro w prawo"},
                                {"direction": "prosto", "distance": "3:", "hint": "kieruj się prosto"},
                                {"direction": "w lewo", "distance": "1", "hint": "skręć w prawo w kierunku sali 105"},
                                {"direction": "prosto", "distance": "5", "hint": "kieruj się prosto w stronę sali 105"},
                                {"direction": "w lewo", "distance": "1", "hint": "skręc w prawo w kierunku sali 106"}
                            ]
                }
            else:
                return {"message": "not hardcoded version of endpoint"}
        return {"message": "not valid data"}
