from flask import Flask, render_template, request
from logic import students, classrooms, preferences

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


@app.route('/classroom_list')
def my_classrooms():
    return render_template("classroom_list.html")


@app.route('/students_list')
def my_students():
    return render_template("students_list.html")

# ________________________________________________________________________________________________________
# Functions
@app.route('/getstudentlists', methods=["POST","GET"])
def testfn():
    if request.method == "POST":
        print(request.form["result"])
        print(students.get_student_list(request.form["result"]))
        return students.get_student_list(request.form["result"])
        #return render_template("students_list.html")
    elif request.method == "GET":
        return students.get_all_student_lists()


@app.route('/getclassroomlists', methods=["GET"])
def testfn2():
    return classrooms.get_all_classroom_lists()


@app.route('/getpreflists', methods=["GET"])
def testfn3():
    return preferences.get_all_pref_lists()


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
