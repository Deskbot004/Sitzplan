from flask import Flask, render_template, request
from logic import students, classrooms, preferences

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


@app.route('/classroom_edit')
def hello2():
    return render_template("classroom_editor.html")


@app.route('/students_class')
def my_students():
    return render_template("students_class.html")

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


@app.route('/getclassroomlists', methods=["POST", "GET"])
def testfn2():
    if request.method == "POST":
        return classrooms.get_classroom_untrimmed(request.form["result"])
    elif request.method == "GET":
        return classrooms.get_all_classroom_lists()


@app.route('/getpreflists', methods=["GET"])
def testfn3():
    return preferences.get_all_pref_lists()


@app.route("/classroom_info", methods=["POST"])
def classroom_info():
    if request.method == "POST":
        classroom_dict = request.form
        classrooms.save_classroom(classroom_dict["name"], classroom_dict["layout_untrimmed"], classroom_dict["layout"])
        return "", 204


@app.route("/delclassroom", methods=["POST"])
def delclassroom():
    if request.method == "POST":
        classrooms.delete_classroom_web(request.form["result"])
        return "", 204


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
