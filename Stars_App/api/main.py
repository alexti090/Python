from flask import Flask, request, jsonify
from data import data

app = Flask(__name__)

@app.route("/")
def home():
  return jsonify({"data": data})

@app.route("/search")
def search():
  name = request.args.get("name")
  star = next(item for item in data if item["name"].lower() == name.lower())
  return star

if __name__ == "__main__":
  app.run(debug=True)