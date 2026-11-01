import os
from dotenv import load_dotenv
from pymongo import MongoClient
import json
from pathlib import Path
from flask import Flask, jsonify, render_template,request

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["flask_assignment"]
collection = db["todo_items"]

app = Flask(__name__)
DATA_FILE = Path(__file__).with_name("data.json")

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/api")
def api():
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return jsonify(json.load(file))

@app.route('/todo')
def todo():
    return render_template('todo.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():

    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')

    if not item_name or not item_description:
        return jsonify({
            "error": "Both fields are required"
        }), 400

    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })

    return jsonify({
        "message": "Data submitted successfully"
    }), 201

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
