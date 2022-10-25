from flask import Flask, render_template, request, send_from_directory
from logic import students, classrooms, preferences
import os

app = Flask(__name__)

#app.config["SERVER_NAME"] = "randomseatings.de:5000"

# Websites
@app.route('/')
def hello():
    return render_template("startsite.html")


@app.route('/home')
def hello6():
    return render_template("startsite.html")


@app.route('/classroom')
def my_classrooms():
    return render_template("classroom_list.html")


@app.route('/seating')
def hello3():
    return render_template("seating.html")


@app.route('/students')
def hello4():
    return render_template("students_list.html")


@app.route('/about')
def hello5():
    return render_template("about.html")


@app.route('/preferences')
def hello7():
    return render_template("preferences_list.html")


@app.route('/from_pref')
def hello9():
    return render_template("preferences_editor.html")


@app.route('/from_classroom')
def hello2():
    return render_template("classroom_editor.html")


@app.route('/from_student')
def my_students():
    return render_template("students_editor.html")

# ________________________________________________________________________________________________________
# Functions
@app.route('/getstudentlists', methods=["POST","GET"])
def testfn():
    if request.method == "POST":
        return students.get_student_list(request.form["result"])
    elif request.method == "GET":
        return students.get_all_student_lists()


@app.route('/student_info', methods=["POST"])
def student_info():
    if request.method == "POST":
        students_dict = request.form
        students.save_students(students_dict["name"], students_dict["students"])
        return "", 204


@app.route("/delstudents", methods=["POST"])
def delstudents():
    if request.method == "POST":
        students.delete_students(request.form["result"])
        return "", 204


@app.route('/getpreflists', methods=["GET", "POST"])
def testfn3():
    if request.method == "POST":
        print(request.form["result"])
        print(preferences.preferences_read(request.form["result"]))
        return preferences.preferences_read(request.form["result"])
    elif request.method == "GET":
        return preferences.get_all_pref_lists()


@app.route("/classroom_info", methods=["POST"])
def classroom_info():
    try:
        if request.method == "POST":
            classroom_dict = request.form
            call = classrooms.save_classroom(classroom_dict["name"], classroom_dict["layout_untrimmed"], classroom_dict["layout"])
            if call == "SUCCESS":
                return "", 204
            else:
                return "", 400
    except Exception as err:
        print(f"Accessing classrooms.py for save failed with {err}")
        return "", 404


@app.route("/delclassroom", methods=["POST"])
def delclassroom():
    try:
        if request.method == "POST":
            call = classrooms.delete_classroom(request.form["result"])
            if call == "SUCCESS":
                return "", 204
            else:
                return "", 400
    except Exception as err:
        print(f"Accessing classrooms.py for delete failed with {err}")
        return "", 404


@app.route('/getclassroomlists', methods=["POST", "GET"])
def getclassroomlists():
    try:
        if request.method == "POST":
            call = classrooms.get_classroom_untrimmed(request.form["result"])
        elif request.method == "GET":
            call = classrooms.get_all_classroom_lists()
        if call[1] == "SUCCESS":
            return call[0], 200
        else:
            return "", 400
    except Exception as err:
        print(f"Accessing classrooms.py for read failed with {err}")
        return "", 404


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
