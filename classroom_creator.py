from flask import Flask, render_template, request
from logic import classrooms

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("classroom.html")


@app.route("/classroom")
def hello2():
    return render_template("classroom.html")


@app.route('/getclassroomlists', methods=["GET"])
def testfn2():
    return classrooms.get_all_classroom_lists()


@app.route("/classroom_info", methods=["POST"])
def classroom_info():
    if request.method == "POST":
        classroom_dict = request.form
        classrooms.save_classroom(classroom_dict["name"], classroom_dict["layout_untrimmed"], classroom_dict["layout"])
        print(classroom_dict)
        return "", 204


@app.route('/classroom_list')
def my_classrooms():
    return render_template("classroom_list.html")


if __name__ == "__main__":
        app.run(
            host="127.0.0.1",
            port=5000,
            debug=True
        )

