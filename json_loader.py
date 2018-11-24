import json
import math
from networkx import Graph


def distance(x_frm, y_frm, x_to, y_to):
    x_diff = x_to - x_frm
    y_diff = y_to - y_frm
    return math.sqrt(x_diff**2 + y_diff**2)


file = open('map.json', 'r')
map = json.load(file)
graph = Graph()

for node in map['vertices']:
    graph.add_node(node[3], x=node[0], y=node[1], type=node[2])

for edge in map['edges']:
    frm = edge[0]
    to = edge[1]
    x_frm = graph.node[frm]['x']
    y_frm = graph.node[frm]['y']
    x_to = graph.node[to]['x']
    y_to = graph.node[to]['y']
    weight = distance(x_frm, y_frm, x_to, y_to)
    graph.add_edge(edge[0], edge[1], weight=weight, type=edge[2])




