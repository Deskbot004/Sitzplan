from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>web test<h1>'


def testpage(name):
        return f

if __name__ == "__main__":
        app.run()

