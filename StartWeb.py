from flask import Flask, render_template, request
from logic import students, classrooms, preferences, generator

app = Flask(__name__)

#app.config["SERVER_NAME"] = "randomseatings.de:5000"

# Websites
@app.route('/')
def start():
    return render_template("startsite.html")


@app.route('/home')
def switch_home():
    return render_template("startsite.html")


@app.route('/classroom')
def switch_classroom():
    return render_template("classroom_list.html")


@app.route('/seating')
def switch_seating():
    return render_template("seating_list.html")


@app.route('/student')
def switch_student():
    return render_template("students_list.html")


@app.route('/about')
def switch_about():
    return render_template("about.html")


@app.route('/preferences')
def switch_preferences():
    return render_template("preferences_list.html")


@app.route('/from_pref')
def from_pref():
    return render_template("preferences_editor.html")


@app.route('/from_classroom')
def from_classroom():
    return render_template("classroom_editor.html")


@app.route('/from_student')
def from_students():
    return render_template("students_editor.html")


@app.route('/from_seating')
def from_seating():
    return render_template("seating_editor.html")


# ________________________________________________________________________________________________________
# Functions students
@app.route('/getstudentlists', methods=["POST","GET"])
def get_students_lists():
    try:
        if request.method == "POST":
            call = students.get_student_list(request.form["result"])
        elif request.method == "GET":
            call = students.get_all_student_lists()
        if call[1] == "SUCCESS":
            return call[0], 200
        else:
            return "", 404
    except Exception as err:
        print(f"Accessing students.py for delete failed with {err}")
        return "", 404


@app.route('/student_info', methods=["POST"])
def student_info():
    try:
        if request.method == "POST":
            students_dict = request.form
            call = students.save_students(students_dict["name"], students_dict["students"])
            if call == "SUCCESS":
                return "", 204
            else:
                return "", 404
    except Exception as err:
        print(f"Accessing students.py for delete failed with {err}")
        return "", 404


@app.route("/delstudent", methods=["POST"])
def del_students():
    try:
        if request.method == "POST":
            call = students.delete_students(request.form["result"])
            if call == "SUCCESS":
                return "", 204
            else:
                return "", 404
    except Exception as err:
        print(f"Accessing students.py for delete failed with {err}")
        return "", 404


# ________________________________________________________________________________________________________
# Functions classroom
@app.route("/classroom_info", methods=["POST"])
def classroom_info():
    try:
        if request.method == "POST":
            classroom_dict = request.form
            call = classrooms.save_classroom(classroom_dict["name"], classroom_dict["layout_untrimmed"], classroom_dict["layout"])
            if call == "SUCCESS":
                return "", 204
            else:
                return "", 404
    except Exception as err:
        print(f"Accessing classrooms.py for save failed with {err}")
        return "", 404


@app.route("/delclassroom", methods=["POST"])
def del_classroom():
    try:
        if request.method == "POST":
            call = classrooms.delete_classroom(request.form["result"])
            if call == "SUCCESS":
                return "", 204
            else:
                return "", 404
    except Exception as err:
        print(f"Accessing classrooms.py for delete failed with {err}")
        return "", 404


@app.route('/getclassroomlists', methods=["POST", "GET"])
def get_classroom_lists():
    try:
        if request.method == "POST":
            call = classrooms.get_classroom_untrimmed(request.form["result"])
        elif request.method == "GET":
            call = classrooms.get_all_classroom_lists()
        if call[1] == "SUCCESS":
            return call[0], 200
        else:
            return "", 404
    except Exception as err:
        print(f"Accessing classrooms.py for read failed with {err}")
        return "", 404


# ________________________________________________________________________________________________________
# Functions preferences IN WORK
@app.route('/getpreflists', methods=["GET", "POST"])
def get_pref_lists():
    if request.method == "POST":
        print(request.form["result"])
        print(preferences.preferences_read(request.form["result"]))
        return preferences.preferences_read(request.form["result"])
    elif request.method == "GET":
        return preferences.get_all_pref_lists()


# ________________________________________________________________________________________________________
# Functions seating IN WORK


@app.route('/getseatinglists', methods=["POST"])
def get_seating():
    if request.method == "POST":
        print(request.form["result"])
        return generator.run(request.form["result"])


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
