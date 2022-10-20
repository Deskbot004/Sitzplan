from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("startsite.html")


@app.route('/home')
def hello6():
    return render_template("startsite.html")


@app.route('/classrooms')
def hello2():
    return render_template("classroom.html")


@app.route('/seating')
def hello3():
    return render_template("seating.html")


@app.route('/students')
def hello4():
    return render_template("students.html")


@app.route('/about')
def hello5():
    return render_template("about.html")


if __name__ == "__main__":
        app.run()

