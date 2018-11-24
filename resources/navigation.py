from flask_restful import Resource, reqparse


class GetMe(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('from',
                        type=dict,
                        help='Send starting point qr/room_name')
    parser.add_argument('to',
                        type=dict,
                        help='Send ending point qr/room_name')

    def post(self):
        data = GetMe.parser.parse_args()
        if data:
            if data['from']['id'] == "sala 101" and data['to']['id'] == 'sala 106':
                return {"route":
                            [
                                {"direction": "prosto", "distance": "5m", "hint": "kieruj się prosto w stronę sali 101"},
                                {"direction": "lekko w prawo", "distance": "2m", "hint": "skręć lekko w prawo"},
                                {"direction": "prosto", "distance": "1m", "hint": "kieruj się prosto w kierunku sal 102, 103"},
                                {"direction": "ostro w prawo", "distance": "2m", "hint": "skręć ostro w prawo"},
                                {"direction": "prosto", "distance": "3m:", "hint": "kieruj się prosto"},
                                {"direction": "w lewo", "distance": "1m", "hint": "skręć w prawo w kierunku sali 105"},
                                {"direction": "prosto", "distance": "5m", "hint": "kieruj się prosto w stronę sali 105"},
                                {"direction": "w lewo", "distance": "1m", "hint": "skręc w prawo w kierunku sali 106"}
                            ]
                }
            else:
                return {"message": "not hardcoded version of endpoint"}
        return {"message": "not valid data"}
