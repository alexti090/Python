from flask import Flask, json, jsonify, request
from classifier import getPrediction

app = Flask(__name__)

@app.route('/')
def function():
  return "Hello, World!"

@app.route('/get-prediction', methods=["POST"])
def getPredict():
  img = request.files.get("digit")
  prediction = getPrediction(img)
  return jsonify({"Prediction": prediction}, 200)

if __name__ == "__main__":
  app.run(debug=True)