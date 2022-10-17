from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("test.html")


def testpage(name):
        return f

if __name__ == "__main__":
        app.run()

