

function getInformation(text){
    var info = $.post("/getstudentlists", {"result": text}, function(data) {addDict(data);});
}

function deleteInformation() {
	$.post("/delstudents", { "result": data }, function(data) {switchToStudents();});
};

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

function renameStudent() {
	var new_name = document.getElementById("new_studentname").value;
	if (new_name == old_name) return;
	if(!addElement(new_name)) {
        var popup = document.getElementById("exists_new_student");
        popup.classList.toggle("show");
    }
    deleteElement(old_name);
    addElement(new_name);
    closeDialog();
}

// overwrites names of students from clickable list objects.
function selectElement(event) {
	old_name = event.target.innerHTML;
	document.getElementById("dialog").showModal();
	var dialog_text = document.getElementById("dialog_text");
	dialog_text.innerHTML = dialog_text.innerHTML.replace("free", old_name);
	document.getElementById("new_studentname").value = old_name;
}

function toPref() {
	localStorage.setItem('selected', data);
    window.location = "/from_pref";
}


// delete Student / rename Student: Maybe alert Popup? <-- selectElement(event)
// rename class
// class deletion before creation is possible
// saving a class should either update or create pref_list


function closeDialog() {
	document.getElementById("dialog").close();
	var dialog_text = document.getElementById("dialog_text");
	dialog_text.innerHTML = dialog_text.innerHTML.replace(old_name, "free");
}
