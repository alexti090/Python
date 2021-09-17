from flask import Flask, jsonify, request

app = Flask(__name__)

task = [
    {"id": 0, "title": "2+2", "description": "Add 2 to 2", "status": False},
    {"id": 1, "title": "3+3", "description": "Add 3 to 3", "status": False},
    {"id": 2, "title": "4+4", "description": "Add 4 to 4", "status": False},
]


@app.route("/")
def funct():
    return "Hello"


@app.route("/get-data")
def getData():
    return jsonify({"task": task})


@app.route("/put-data", methods=["POST"])
def putData():
    if not request.json:
        return jsonify({"message": "Please enter the data", "status": "error"}, 200)
    newTask = {
        "id": task[-1]["id"] + 1,
        "title": request.json["title"],
        "description": request.json.get("description", ""),
        "status": False,
    }
    task.append(newTask)
    return jsonify({'message': 'Task added successfuly', 'status': 'success'})

if __name__ == "__main__":
    app.run(debug=True)
