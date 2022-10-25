/*
	This js contains functions called by students_editor.html.


	Functions:
		getInformation(string)
		deleteInformation()
		saveClass()
		?renaming(string, string)
		create_str() -> string
		addStudent()
		renameStudent()
		selectElement(event)
		toPref()
		closeDialog()

	// rename class
	// class deletion before creation is possible
	// saving a class should either update or create pref_list
	// Alphabetical Sorting of student list? Per Button? <- Traceback preflist
*/


/*
	Function to fill 'var_list' with all items from the requested dictionary.

	@param text: Name of the student dict as string
	@return: void
*/
function getInformation(text){
    var info = $.post("/getstudentlists", {"result": text}, function(data) {addDict(data);});
}


/*
	Function to delete the currently student list from the server

	@return: void
*/
function deleteInformation() {
	$.post("/delstudents", { "result": data }, function(data) {switchToStudents();});
};


/*
	Function to save the current configuration of 'var_list' as a .json
	in /data.

	@return: void
*/
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


/*
	A
*/
//maybe use from classroom?
function renaming(data, name) {}


/*
	Function to transform the current 'var_list' to string.
	Used to transfer the dictionary information back to the server.

	@return: String containing the dictionary information
*/
function create_str() {
    var list = document.getElementById('var_list');
    var elements = list.getElementsByTagName("li");
    var student_str = "";

    for ( var i = 0, len = elements.length; i < len; i++) {
        student_str += elements[i].innerHTML + "|";
    }
    return student_str;
}


/*
	Adds a Student from the on site input field.

	@return: void
*/
function addStudent() {
    if(!addElement(document.getElementById('studentname').value)) {
        var popup = document.getElementById("exists_student");
        popup.classList.toggle("show");
    }
}


/*
	Renames a student from the opened dialog window.

	@return: void
*/
function renameStudent() {
	var new_name = document.getElementById("new_studentname").value;
	if (new_name == old_name) return;
	if(!addElement(new_name)) {
        var popup = document.getElementById("exists_new_student");
        popup.classList.toggle("show");
        return
    }
    deleteElement(old_name);
    addElement(new_name);
    closeDialog();
}


/*
	Opens a dialog window, when a student is clicked.

	@param event: The click event
	@return: void
*/
function selectElement(event) {
	old_name = event.target.innerHTML;
	document.getElementById("dialog").showModal();
	var dialog_text = document.getElementById("dialog_text");
	dialog_text.innerHTML = dialog_text.innerHTML.replace("free", old_name);
	document.getElementById("new_studentname").value = old_name;
}


/*
	Switches the location to the editing of the preference list of the current class.

	@return: void
*/
function toPref() {
	localStorage.setItem('selected', data);
    window.location = "/from_pref";
}


/*
	Closes the dialog window and resets its title.

	@return: void
*/
function closeDialog() {
	document.getElementById("dialog").close();
	var dialog_text = document.getElementById("dialog_text");
	dialog_text.innerHTML = dialog_text.innerHTML.replace(old_name, "free");
}
