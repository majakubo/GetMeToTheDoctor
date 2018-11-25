from networkx import dijkstra_path, Graph
import math
import math


def navigation_description(graph, frm, to):
    path = dijkstra_path(graph, frm, to, 'weight')
    edges_path = convert_to_edges(path)
    weights = weight_of_edges(graph, edges_path)
    directions = directions_of_edges(graph, path)
    rooms = find_rooms_along_the_way(graph, path)
    navigated_path = list(zip(directions, weights, rooms))
    return parse_guided_path(simplify_path(navigated_path))


def parse_guided_path(simplified_path):
    guided_path = []
    for step in simplified_path:
        direction, weight, rooms = step
        hint = parse_neighbors_to_hint(rooms)
        guided_path.append({"direction": direction, "distance": weight})
    return guided_path


def parse_neighbors_to_hint(rooms):
    if rooms:
        hint = "Kieruj sie w strone {}".format(rooms[0])
        if len(rooms) > 1:
            rooms_str = "sal "
            for room in rooms[1:]:
                rooms_str += str(room)

            hint = hint + " przejdz obok " + rooms_str

        return hint

    return ""


def convert_to_edges(route):
    edge_route = []
    for i in range(len(route) - 1):
        node_id = route[i]
        next_node_id = route[i + 1]
        edge = [node_id, next_node_id]
        edge_route.append(edge)
    return edge_route


def find_rooms_incident(graph, node):
    rooms = []
    for neighbor in g.neighbors(node):
        if g.nodes[neighbor]['type'] == 'room':
            rooms.append(neighbor)
    return rooms


def find_rooms_along_the_way(graph, path):
    rooms = []
    for node in path:
        neighbors = list(graph.neighbors(node))
        position = []
        for neighbor in neighbors:
            if graph.nodes[neighbor]['type'] == 'room':
                position.append(neighbor)
        rooms.append(position)
    return rooms


def simplify_path(path):
    simplified_path = []
    summary = 0
    rooms = []
    for edge in path:
        direction, weight, neighbors = edge
        if direction == 'Straight':
            summary += weight
            rooms = rooms + neighbors
        else:
            simplified_path.append(('Straight', summary, neighbors))
            summary = 0
            neighbors = []
            simplified_path.append(edge)

    if summary > 0:
        simplified_path.append(('Straight', summary))

    print(simplified_path)
    return simplified_path


def weight_of_edges(graph, edges_path):
    weights = []
    for edge in edges_path:
        frm, to = edge
        weight = graph.get_edge_data(frm, to)['weight']
        weights.append(int(weight))
    return weights


def directions_of_edges(graph, path):
    directions = ['Straight']
    for i in range(len(path) - 2):
        before_x = graph.nodes[path[i]]['x']
        before_y = graph.nodes[path[i]]['y']
        current_x = graph.nodes[path[i + 1]]['x']
        current_y = graph.nodes[path[i + 1]]['y']
        next_x = graph.nodes[path[i + 2]]['x']
        next_y = graph.nodes[path[i + 2]]['y']
        dir = direction(before_x, before_y, current_x, current_y, next_x, next_y)
        directions.append(dir)

    return directions


def direction(x_before, y_before, x_corner, y_corner, x_next, y_next):
    a = (y_corner - y_before) / (x_corner - x_before)
    b = (y_before - a * x_before)
    path_to_corner = (x_corner - x_before, y_corner - y_before)
    path_after_corner = (x_next - x_corner, (y_next - y_corner))
    scalar = path_to_corner[0] * path_after_corner[0] + path_to_corner[1] * path_after_corner[1]
    len_path_to_corner = math.sqrt(path_to_corner[0] ** 2 + path_to_corner[1] ** 2)
    len_path_after_corner = math.sqrt(path_after_corner[0] ** 2 + path_after_corner[1] ** 2)
    if y_next < ((a * x_next) + b):  # to jest skret w prawo
        deg = math.acos((scalar) / (len_path_after_corner) * (len_path_to_corner))
        deg = deg * (180 / math.pi)
        if deg >= 0 and deg <= 70:
            return "Sharp Right"
        elif deg > 70 and deg <= 110:
            return "Right"
        elif deg > 110 and deg <= 160:
            return "Slight Right"
        elif deg > 160 and deg <= 180:
            return "Straight"
    elif y_next > ((a * x_next) + b):  # to jest skret w lewo
        deg = math.acos((scalar) / (len_path_after_corner) * (len_path_to_corner))
        deg = deg * (180 / math.pi)
        if deg >= 0 and deg <= 70:
            return "Light Left"
        elif deg > 70 and deg <= 110:
            return "Left"
        elif deg > 110 and deg <= 160:
            return "Sharp Left"
        elif deg > 160 and deg <= 180:
            return "Straight"
    else:
        return "Straight"
