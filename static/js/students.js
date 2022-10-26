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
	//everything below nearly identical to classroom.js????
	Asynchronous Functions:
		deleteInformation()
		saveClass()
		renaming(string, string)
	Requests:
		requestInformation(text) -> request
		deleteInformation() -> request
		renameRequest()


	// rename class
	// class deletion before creation is possible
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
			addDict(student_info);
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





//_________________________________Asynchronous Functions________________________________________________




/*
    Deletes the current classroom from the server.

    @return: void
*/
async function deleteInformation() {
	try {
		var error_case = "undefined";
		var rename_request = renameRequest();
		rename_request.done(function(data) {
	        console.log("Data has been collected from server!");
	    });
		rename_request.fail(function(xhr, status, error) {
	        error_case = "ERROR " + error.toString();
	    });
		var data_dict = await rename_request;

		var found = 0;
		for (var elem of Object.keys(data_dict)) {
	        if(data_dict[elem] == data) found = 1;
	    }

		if (!found) throw "not_created";
		if (!ask_delete()) throw "canceled";

	    var delete_return = deleteRequest(data);
	    delete_return.done(function(data) {
	        switchToStudents();
	    });
	    delete_return.fail(function(xhr, status, error) {
	        error_case = "ERROR " + error.toString();
	    });
	    await delete_return;
	} catch(err) {
		switch(err) {
			case 'not_created':
				err_text = "The classroom was never saved!"; break;
			case 'canceled':
				err_text = "Deleting was canceled!"; break;
			default:
				err_text = "Deleting Information went wrong! The room was not deleted!"; break;
		}

		var popup = document.getElementById("popup_del");
		popup.innerHTML = err_text;
		popup.classList.toggle("show");

		switch(typeof err) {
			case "string":
				console.log("Function deleteInformation failed with " + err);break;
			case "object":
				console.log("Delete request failed with "+ error_case);
				console.log(err);
				break;
			default:
				console.log("Undetected Error type: " + typeof err);break;
		}
	}
};


//TODO UPDATE THIS SHIT
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




//_________________________________Requests______________________________________________________________




/*
	Request to get student list information.

	@param text: Name of the student dict as string
	@return: Request
*/
function requestInformation(text){
    return $.post("/getstudentlists", {"result": text});
};


/*
	Request to delete a student list.

	@return: Request
*/
function deleteRequest() {
	return $.post("/delstudents", {"result": data});
};


/*
	Requests the list of all students

	@param text: List of the classes
	@return: Request
*/
function renameRequest() {
    return $.get("/getstudentlists");
};