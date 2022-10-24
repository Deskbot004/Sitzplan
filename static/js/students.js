

function getInformation(text){
    var info = $.post("/getstudentlists", {"result": text}, function(data) {addDict(data);});
}

function saveClass() {
    //check name
    var name = document.getElementById("filename").value;

    if (!checkForIllegalCharacters(name)) {
        var popup = document.getElementById("illegal");
        popup.classList.toggle("show");
        return;
    }

    //check if var_list empty
    if(document.getElementById('var_list').innerHTML.trim() == "") {
        var popup = document.getElementById("empty");
        popup.classList.toggle("show");
        return;
    }


    /*
        check if renaming is needed
    if (name != data) {
        if(!renaming(data, name)) return;
    }

    */

    //save class
    var popup = document.getElementById("saved");
    popup.classList.toggle("show");


    var student_str = create_str();
    data = name;

	var result = {"name" : name, "students": student_str};

    $.post("/student_info",
            {"name" : name, "students": student_str},
            function(data) {});
}

//maybe use from classroom?
function renaming(data, name) {}

function create_str() {
    var list = document.getElementById('var_list');
    var elements = list.getElementsByTagName("li");
    var student_str = "";

    for ( var i = 0, len = elements.length; i < len; i++) {
        student_str += elements[i].innerHTML + "|";
    }
    return student_str;
}

function addStudent() {
    if(!addElement(document.getElementById('studentname').value)) {
        var popup = document.getElementById("exists_student");
        popup.classList.toggle("show");
    }
}

// delete Student / rename Student: Maybe alert Popup?