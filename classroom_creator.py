from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("classroom.html")


@app.route("/classroom_info", methods=["POST"])
def classroom_info():
    if request.method == "POST":
        print(request.form)
        return "", 204


if __name__ == "__main__":
        app.run(
            host="127.0.0.1",
            port=5000,
            debug=True
        )

