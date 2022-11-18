/*
	This js contains functions called by students_editor.html.


	Simple functions on html:
		create_str()
	Functions from user interaction:
		getInformation(string)
		addStudent()
		renameStudent()
		selectElement(event)
		closeDialog()

	// saving a class should either update or create pref_list
	// Alphabetical Sorting of student list? Per Button? <- Traceback preflist
*/




//_________________________________Simple functions on html______________________________________________




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




//_________________________________Functions from user interaction_______________________________________




/*
    Loads the information of a given classroom list

	TODO

    @return: void
*/
async function getInformation(text) {
    // TODO change fill method
    identity = "pref";
    var room_list = document.getElementById("pref_list");
    room_list.id = "var_list";

    var req_prefs = requestInformation(data);
	req_prefs.done( function(pref_info) {
		addDict(pref_info, 0);
	});

    await req_prefs;
    room_list.id = "pref_list";


    identity = "student";
	var stud_list = document.getElementById("stud_list");
	stud_list.id = "var_list";

	var req_studs = requestInformation(data);
	req_studs.done( function(studs_info) {
		addDict(studs_info, 0);
	});
	req_studs.fail( function(){
		console.log("No file named " + text + " found, loading template.");
		stud_list.id = "stud_list";
		document.getElementById('studentname').value = "Max Mustermann";
		addStudent();
		document.getElementById('studentname').value = "Student";
	});

    await req_studs;
    stud_list.id = "stud_list";

    document.getElementById('head_text').innerHTML = document.getElementById('head_text').innerHTML.replace("free", data);
    document.getElementById('filename').value = data;
};


/*
	Adds a Student from the on site input field.

	@return: void
*/
function addStudent() {
	try {
		var stud_list = document.getElementById("stud_list");
		stud_list.id = "var_list";
	    if(!addElement(document.getElementById('studentname').value, 1)) throw "exists"
	    stud_list.id = "stud_list";

		// TODO change fill method
	     var room_list = document.getElementById("pref_list");
        room_list.id = "var_list";
        addElement("empty,empty,empty,empty,empty", 0)
        room_list.id = "pref_list";

	} catch (err) {
		switch (err) {
			case "exists":
				err_text = "This student already exists!"; break;
			default:
				err_text = "Adding student went wrong! The student was not added!"; break;
		}
		console.log("Function addStudent failed with " + err);
		var popup = document.getElementById("popup_add");
		popup.innerHTML = err_text;
	    popup.classList.toggle("show");
	}
}

function deleteStudent(){
	var stud_list = document.getElementById("stud_list");
	stud_list.id = "var_list";
    deleteElement(old_name);
	closeDialog()
    stud_list.id = "stud_list";

    //TODO Remove entry on preflist
}

/*
	Renames a student from the opened dialog window.

	@return: void
*/
function renameStudent() {
	try {
		var stud_list = document.getElementById("stud_list");
		stud_list.id = "var_list";

		var new_name = document.getElementById("new_studentname").value;
		if (new_name == old_name) return;
		if(!addElement(new_name, 1)) throw "exists";
	    deleteElement(old_name);
	    closeDialog();

	    stud_list.id = "stud_list";


	    // TODO add interaction with preflist
	} catch(err) {
		switch (err) {
			case "exists":
				err_text = "This student already exists!"; break;
			default:
				err_text = "Adding student went wrong! The student was not added!"; break;
		}
		console.log("Function renameStudent failed with " + err);
		var popup = document.getElementById("popup_rename");
		popup.innerHTML = err_text;
	    popup.classList.toggle("show");
	}
}


/*
	Opens a dialog window, when a student is clicked.

	@param event: The click event
	@return: void
*/
function selectElement(event) {
	try {
		old_name = event.target.innerHTML;
		document.getElementById("dialog").showModal();
		var dialog_text = document.getElementById("dialog_text");
		dialog_text.innerHTML = dialog_text.innerHTML.replace("free", old_name);
		document.getElementById("new_studentname").value = old_name;
	} catch (err) {
		alert("Selecting element went wrong! The element was not selected!");
		console.log("Function selectElement failed with " + err);
	}
}


/*
	Closes the dialog window and resets its title.

	@return: void
*/
function closeDialog() {
	try {
		document.getElementById("dialog").close();
		var dialog_text = document.getElementById("dialog_text");
		dialog_text.innerHTML = dialog_text.innerHTML.replace(old_name, "free");
	} catch (err) {
		alert("Closing dialog went wrong! The dialog was not closed!");
		console.log("Function closeDialog failed with " + err);
	}
}


/*
	Function to test specific edge cases before sending the information to generic saveData().

	@return: void
*/
function pre_saveData() {
	try {
		var stud_list = document.getElementById("stud_list");
		stud_list.id = "var_list";

		var error_case = "Not request fail";

		if(document.getElementById('var_list').innerHTML.trim() == "") throw "empty";

	    var name = document.getElementById("filename").value;
		var student_str = create_str();

	    saveData({"name" : name, "students": student_str});

		stud_list.id = "stud_list";
	    //TODO update preflists when everything went fine

		var pref_list = document.getElementById("pref_list");
		pref_list.id = "var_list";
		identity = "pref"

		var pref_str = create_str();

		saveData({"name" : name, "students": pref_str});

		pref_list.id = "room_list";
		identity = "student"

	} catch (err) {
		switch(err) {
			case 'empty':
				err_text = "The class is empty!"; break;
			default:
				err_text = "Saving class went wrong! The class has not been saved!"; break;
		}

		switch(typeof err) {
			case "string":
				if(err != "saved") console.log("Function pre_sendData failed with " + err);break;
			case "object":
				console.log("Save request failed with "+ error_case);
				console.log(err);
				break;
			default:
				console.log("Undetected Error type: " + typeof err);break;
		}

		var popup = document.getElementById("popup_save");
		popup.innerHTML = err_text;
		popup.classList.toggle("show");
	}
}

// TODO configure deleting preflists
function deleteClass(){
	deleteInformation();
}