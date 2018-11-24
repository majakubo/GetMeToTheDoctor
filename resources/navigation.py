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
        print("in post")
        data = GetMe.parser.parse_args()
        print("you start at {} which is {}".format(data['from']['value'], data['from']['type']))
        print("you end at {} which is {}".format(data['to']['value'], data['to']['type']))
        return {"message": "is it your mistake or mine"}