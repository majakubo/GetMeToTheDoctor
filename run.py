from app import app
from db import db
from scripts.json_loader import load_offices_to_database, load_graph_to_memory

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()
    graph = load_graph_to_memory('map.json')
    load_offices_to_database(graph)

