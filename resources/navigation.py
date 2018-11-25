from flask_restful import Resource, reqparse
from models.doctors import Doctor
from models.offices import Office
from models.shifts import Shift
from scripts.json_loader import load_graph_to_memory
from networkx import Graph
from scripts.path_finder import navigation_description
class GetMe(Resource):
    graph = load_graph_to_memory('map.json')
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
            if data['from']['type'] == 'Room':
                frm = data['from']['id']
            elif data['from']['type'] == 'QR':
                frm = data['from']['id']

            if data['to']['type'] == 'Room':
                to = data['to']['id']
            elif data['to']['type'] == 'Doctor':
                to = None
            print("from {} to {}".format(frm, to))

            return navigation_description(GetMe.graph, int(frm), int(data['to']['id']))

        else:
            return {"message": "not valid params"}

