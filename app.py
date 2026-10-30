import json
from pathlib import Path
from flask import Flask, jsonify, render_template

app = Flask(__name__)
DATA_FILE = Path(__file__).with_name("data.json")

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/api")
def api():
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return jsonify(json.load(file))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
