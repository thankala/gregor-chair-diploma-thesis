from flask import Flask

app = Flask(__name__)

@app.route("/move")
def move():
    return "<p>Move!</p>"

@app.route("/1")
def pick_and_flip_and_press():
    return "<p>Pick and Flip and Press</p>"

@app.route("/2")
def pick_and_insert():
    return "<p>Pick and Insert</p>"

@app.route("/3")
def pick_and_place():
    return "<p>Pick and place</p>"

@app.route("/4")
def screw_pick_and_fasten():
    return "<p>Screw pick and fasten</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")    