import json

def load_db():
    with open("dataBase-json.json") as f:
        return json.load(f)
    
db = load_db()