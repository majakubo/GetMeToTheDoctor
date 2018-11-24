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
                        help='Send ending point qr/room_name')

    def post(self):
        data = GetMe.parser.parse_args()
        print("you start at {} which is {}".format(data['from']['value'], data['from']['type']))
        print("you end at {} which is {}".format(data['to']['value'], data['to']['type']))
