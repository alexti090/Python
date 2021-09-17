from flask import Flask, jsonify, request

app = Flask(__name__)

phonebook = [{"Contact": "0123456789", "Name": "John Doe", "ID": 1}]

@app.route("/")
def appFunc():
  return "Add '/get-data' at the end of the url to get the list of phone numbers."

@app.route("/get-data")
def getData():
  return jsonify({"Phonebook": phonebook})

@app.route("/add-data", methods=["POST"])
def addData():
  if not request.json:
    return jsonify({"Message": "Please enter the data.", "Status": "ERROR"})

  phonebook.append({
    "Contact": request.json["Contact"],
    "Name": request.json["Name"],
    "ID": phonebook[-1]["ID"] + 1,
  })

  return jsonify({"Message": "Data added successfuly", "Status": "success"})

if __name__ == "__main__":
  app.run(debug=True)