from networkx import dijkstra_path, Graph
import math
import math


def navigation_description(graph, frm, to):
    path = dijkstra_path(graph, frm, to, 'weight')
    edges_path = convert_to_edges(path)
    weights = weight_of_edges(graph, edges_path)
    directions = directions_of_edges(graph, path)
    print(directions)
    rooms = find_rooms_along_the_way(graph, path)
    navigated_path = list(zip(directions, weights, rooms))
    return parse_guided_path(simplify_path(navigated_path))


def parse_guided_path(simplified_path):
    guided_path = []
    for step in simplified_path:
        direction, weight, rooms = step
        hint = parse_neighbors_to_hint(rooms)
        guided_path.append({"direction": direction, "distance": weight, "hint": hint})
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
        if graph.nodes[neighbor]['type'] == 'room':
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
        dir = gimme_direction((-before_x, before_y), (-current_x, current_y), (-next_x, next_y))
        directions.append(dir)

    return directions



def gimme_direction(before, corner, after):
    directions = [
        'turn-around',
        'Sharp left',
        'Left',
        'Slight left',
        'Straight',
        'Slight right',
        'Right',
        'Sharp-right']

    second_triangle = (after[0] - corner[0], after[1] - corner[1])
    first_triangle = (before[0] - corner[0], before[1] - corner[1])
    angle2 = math.degrees(math.atan2(second_triangle[1], second_triangle[0]))
    angle1 = math.degrees(math.atan2(first_triangle[1], first_triangle[0]))
    if angle1 < 0:
        angle1 = 360 + angle1
    if angle2 < 0:
        angle2 = 360 + angle2
    angle = angle1 - angle2
    if angle < 0:
        angle = 360 + angle
    print(angle)
    index = round(angle / 45) % 8
    return directions[index]




