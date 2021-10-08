from flask import Flask, request, jsonify
from data import data

app = Flask(__name__)

@app.route("/")
def func1():
  return jsonify({"data": data})

@app.route("/planet")
def func2():
  name = request.args.get("name")
  planetdata = next(item for item in data if item["name"] == name)
  return planetdata


if __name__ == "__main__":
  app.run(debug=True)