from app import app
from db import db
from scripts.json_loader import load_offices_to_database

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()


