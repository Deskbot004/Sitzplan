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

    @return: void
*/
function getInformation(text) {
	try {
		var req_students = requestInformation(text);
		req_students.done( function(students_info) {
			addDict(students_info);
		});
		req_students.fail( function(){
			console.log("No file named " + text + " found, loading template.");
			addDict({1: "Max Mustermann"});
		});
	} catch(err) {
		alert("Getting Information went wrong! The student list was not properly loaded!");
		console.log("Function getInformation failed with " + err);
	}
};


/*
	Adds a Student from the on site input field.

	@return: void
*/
function addStudent() {
	try {
	    if(!addElement(document.getElementById('studentname').value)) throw "exists"
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


/*
	Renames a student from the opened dialog window.

	@return: void
*/
function renameStudent() {
	try {
		var new_name = document.getElementById("new_studentname").value;
		if (new_name == old_name) return;
		if(!addElement(new_name)) throw "exists";
	    deleteElement(old_name);
	    closeDialog();
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
		var error_case = "Not request fail";

		if(document.getElementById('var_list').innerHTML.trim() == "") throw "empty";

	    var name = document.getElementById("filename").value;
		var student_str = create_str();

	    saveData({"name" : name, "students": student_str});

	    //TODO update preflists when everything went fine

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


/*
	Function which on load fills both lists with the existing information.

	TODO

	@return: void
*/
async function fillLists() {
    var stud_list = document.getElementById("stud_list");
    stud_list.id = 'var_list';
    await getLists();
    stud_list.id = "stud_list";

    identity = "classroom";
    var room_list = document.getElementById("room_list");
    room_list.id = "var_list";
    await getLists();
    room_list.id = "room_list";

    identity = "student";
};
