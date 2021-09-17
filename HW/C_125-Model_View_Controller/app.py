from flask import Flask, json, jsonify, request
from classifier import getPred

app = Flask(__name__)

@app.route('/')
def function():
  return "Hello, World!"

@app.route('/get-prediction', methods=["POST"])
def getPredict():
  img = request.files.get("alphabet")
  prediction = getPred(img)
  return jsonify({"Prediction": prediction})

if __name__ == "__main__":
  app.run(debug=True)