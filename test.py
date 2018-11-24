from scripts.json_loader import load_graph_to_memory
from scripts.path_finder import *
g = load_graph_to_memory('map.json')
print(find_path_with_description(g, 165, 150))
