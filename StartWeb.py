from flask import Flask, render_template, request
from logic import students, classrooms, generator, data_manager

app = Flask(__name__)
data_dict = {}
back_up_dict = {}


# app.config["SERVER_NAME"] = "randomseatings.de:5000"

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


@app.route('/from_classroom')
def from_classroom():
    return render_template("classroom_editor.html")


@app.route('/from_student')
def from_students():
    return render_template("students_editor.html")


@app.route('/from_seating')
def from_seating():
    return render_template("seating_editor.html", user_image="static/images/working.png")


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
            new_data = students.string_converter(students_dict["students"])
            call = students.save_students(students_dict["name"], new_data)
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
            call = classrooms.save_classroom(classroom_dict["name"], classroom_dict["layout"])
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
            call = classrooms.get_classroom(request.form["result"])
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
# Functions preferences !! should be irrelevant with new rework!
"""
@app.route('/getpreflists', methods=["GET", "POST"])
def get_pref_lists():
    if request.method == "POST":
        return preferences.preferences_read(request.form["result"])
    elif request.method == "GET":
        return preferences.get_all_pref_lists()


@app.route('/pref_info', methods=["POST"])
def pref_info():
    try:
        if request.method == "POST":
            pref_dict = request.form
            call = preferences.save_preferences(pref_dict["name"], pref_dict["students"])
            if call == "SUCCESS":
                return "", 204
            else:
                return "", 404
    except Exception as err:
        print(f"Accessing students.py for delete failed with {err}")
        return "", 404


@app.route("/delpref", methods=["POST"])
def del_pref():
    try:
        if request.method == "POST":
            call = preferences.preferences_delete(request.form["result"])
            if call == "SUCCESS":
                return "", 204
            else:
                return "", 404
    except Exception as err:
        print(f"Accessing preferences.py for delete failed with {err}")
        return "", 404
"""

# ________________________________________________________________________________________________________
# Functions seating IN WORK


@app.route('/getseatinglists', methods=["POST"])
def get_seating():
    if request.method == "POST":
        call = generator.run(request.form["result"])
        return call[0], 200


# ________________________________________________________________________________________________________
# Functions upload handling


@app.route('/upload', methods=["POST"])
def upload():
    gotten_files = request.files
    list = gotten_files["files[]"]
    students.read_from_upload(list.read(), list.mimetype, list.filename)
    return switch_about()


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


def create_backup():
    global data_dict
    global back_up_dict
    back_up_dict = data_dict


# For some reason the main gets called twice on startup, but idk....
if __name__ == "__main__":
    try:
        data_dict = data_manager.ini_dict(data_dict)
        app.run(
            host="0.0.0.0",
            # Aus Railway
            port=5000,
            debug=True
        )
    finally:
        print("Saving dict:")
        print(data_manager.save_dict(data_dict))
