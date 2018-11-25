from networkx import dijkstra_path, Graph
import math
import math
def find_path_with_description(graph, frm, to):
    route = dijkstra_path(graph, frm, to, 'weight')
    edges_path = convert_to_edges(route)
    add_weight_to_edges(graph, edges_path)
    add_directions(graph, edges_path)
    return edges_path

def convert_to_edges(route):
    edge_route = []
    for i in range(len(route) - 1):
        node_id = route[i]
        next_node_id = route[i + 1]
        edge = [node_id, next_node_id]
        edge_route.append(edge)
    return edge_route


def add_weight_to_edges(graph, edges_path):
    for i in range(len(edges_path)):
        frm, to = edges_path[i]
        weight = graph.get_edge_data(frm, to)['weight']
        edges_path[i].append(("weight", int(weight)))


def add_directions(graph, edges_path):
    for i in range(len(edges_path)):
        frm, to = edges_path[i][0], edges_path[i][1]
        deg = calculate_direction(graph, frm, to)
        edges_path[i].append(("deg", deg))


def calculate_degree(graph, frm, to):
    x_frm = graph.node[frm]['x']
    y_frm = graph.node[frm]['y']
    x_to = graph.node[to]['x']
    y_to = graph.node[to]['y']
    relative_x = x_to - x_frm
    relative_y = y_to - y_frm
    return math.atan2(relative_y, relative_x) * 180/math.pi


def calculate_direction(graph, frm, to):
    deg = int(calculate_degree(graph, frm, to))
    if deg < 0:
        deg = 360 - deg

    if deg > 70 and deg < 110:
        return "Prosto"
    elif (deg <= 340 and deg <= 360) or (deg >= 0 and deg <= 20):
        return "Prawo"
    elif deg >= 160 and deg <= 200:
        return "Lewo"
    elif deg > 20 and deg < 70:
        return "Lekko w prawo"
    elif  deg > 110 and deg < 160:
        return "Lekko w lewo"
    elif deg > 200 and deg < 270:
        return "Ostro w lewo"
    elif deg > 270 and deg < 340:
        return "Ostro w prawo"



def add_hints(route):
    pass

def render_route(route):
    pass



def direction_wrapper(graph, before, corner, after):
    return direction(graph.node[before]['x'], graph.node[before]['y'],
                     graph.node[corner]['x'], graph.node[corner]['y'],
                     graph.node[after]['x'], graph.node[after]['y']
                     )

def direction(x_before, y_before, x_corner, y_corner, x_next, y_next):
    path_to_corner = (x_corner - x_before, y_corner - y_before)
    path_after_corner = (x_next - x_corner, (y_next - y_corner))
    scalar = path_to_corner[0]*path_after_corner[0] + path_to_corner[1]*path_after_corner[1]
    len_path_to_corner = math.sqrt(path_to_corner[0]**2 + path_to_corner[1]**2)
    len_path_after_corner = math.sqrt(path_after_corner[0]**2 + path_after_corner[1]**2)

    deg = math.acos((scalar)/(len_path_after_corner)*(len_path_to_corner))
    deg = deg * 180/math.pi

    if deg >= 0 and deg <= 60:
        return "Ostry Skret Prawo"
    elif deg > 60 and deg <= 110:
        return "w Prawo"
    elif deg > 110 and deg <= 160:
        return "Lekki skret w prawo"
    elif deg > 160 and deg <= 200:
        return "Prosto"
    elif deg > 200 and deg <= 250:
        return "Lekki skret w lewo"
    elif deg > 250 and deg <= 290:
        return "skre w Lewo"
    elif deg > 290 and deg < 360:
        return "Ostry skret w lewo"
