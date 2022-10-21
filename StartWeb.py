from flask import Flask, render_template, request
from logic import students, classrooms

app = Flask(__name__)


# Websites
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


# ________________________________________________________________________________________________________
# Functions
@app.route('/getstudentlists', methods=["GET"])
def testfn():
    return students.get_all_student_lists()


@app.route("/classroom_info", methods=["POST"])
def classroom_info():
    if request.method == "POST":
        classroom_dict = request.form
        classrooms.save_classroom(classroom_dict["name"], classroom_dict["layout_untrimmed"], classroom_dict["layout"])
        print(classroom_dict)
        return "", 204


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
