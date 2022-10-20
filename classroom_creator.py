from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("classroom.html")


@app.route("/ProcessUserInfo<string:userinfo>", methods=["POST"])
def ProcessUserInfo(userinfo):
    userinfo = json.loads(userinfo)
    print()
    print(userinfo)
    print()
    return "/"


if __name__ == "__main__":
        app.run(debug=True)

