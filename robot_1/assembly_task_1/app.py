from flask import Flask
import requests

app = Flask(__name__)


@app.route("/at1", methods=['GET'])
def assembly_task_1():
    requests.get("http://at1:8080/3")
    requests.get("http://at1:8080/1")
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
