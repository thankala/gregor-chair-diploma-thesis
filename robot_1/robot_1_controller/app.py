from flask import Flask
from services.pick_and_flip_and_press import PickAndFlipAndPress, PickAndInsert, PickAndPlace, ScrewPickAndFasten

app = Flask(__name__)

move1 = PickAndFlipAndPress()
move2 = PickAndInsert()
move3 = PickAndPlace()
move4 = ScrewPickAndFasten()


@app.route("/move")
def move():
    return "<p>Move!</p>"


@app.route("/1", methods=["GET"])
def pick_and_flip_and_press():
    message = move1.start_working()
    if message == 'ok':
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    else:
        response = app.response_class(
            response=json.dumps(data),
            status=500,
            mimetype='application/json'
        )
    return response


@app.route("/2", methods=["GET"])
def pick_and_insert():
    message = move2.start_working()
    if message == 'ok':
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    else:
        response = app.response_class(
            response=json.dumps(data),
            status=500,
            mimetype='application/json'
        )
    return response


@app.route("/3", methods=["GET"])
def pick_and_place():
    message = move3.start_working()
    if message == 'ok':
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    else:
        response = app.response_class(
            response=json.dumps(data),
            status=500,
            mimetype='application/json'
        )
    return response


@app.route("/4", methods=["GET"])
def screw_pick_and_fasten():
    message = move4.start_working()
    if message == 'ok':
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    else:
        response = app.response_class(
            response=json.dumps(data),
            status=500,
            mimetype='application/json'
        )
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
