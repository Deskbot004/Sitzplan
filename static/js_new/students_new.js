/*
	This js contains functions called for students_list.html

	Functions:
        loadInformation() - Loads a list (or similar) from the server
        saveElement() - Saves the Element to the server

    Common Variables:
        list_id - id of a list
	    list_type - type of a list (see below)

    List-Types:
        "dropdown" - Dropdown menu, that gets narrowed down then you type ("type to search")
        "class" - List of all Classes
        "student" - List of all Students in a Class
*/

//_________________________________Functions________________________________________________

async function loadInformation(list_type, name) {
    var list_id = list_type + "_list";

    switch (list_type) {
        case "class":
            var request = listRequest();
            break;
        case "student":
            var request = requestInformation(name);
            localStorage.clear()
            localStorage.setItem("file_name", name);

            // Please keep this line for now as it will be useful when testing the file opened blocking later
            console.log("I am currently viewing the file " + name);

            document.getElementById('class_name').innerHTML = name;
            break;
        case "pref":
            var prefs = localStorage.getItem(name).split(";"); //Load Prefs

            //Input Prefs into corresponding text field
            document.getElementById('pref_name').value = name;
            document.getElementById('pref0').value = prefs[0];
            document.getElementById('pref1').value = prefs[1];
            document.getElementById('pref2').value = prefs[2];
            document.getElementById('pref3').value = prefs[3];

            //Select correct Button (Front/Back/Either)
            switch(prefs[4]) {
                case "1":
                    document.getElementById('Front').checked = "checked";
                    break;
                case "-1":
                    document.getElementById('Back').checked = "checked";
                    break;
                default:
                    document.getElementById('Either').checked = "checked";
            }
            return;
        default:
	        alert("students/loadInformation: type \"" + list_type + "\" not recognized");
    }

    request.done( function(information) {
        if (list_type === "student") {  //TODO: needs a small rework to fit the new format of classes rn preferences get loaded instead
            //Save student prefs to local Storage
            for (student_name of Object.keys(information)) {
                //Example: localStorage.getItem("Jonas") would get all preferences of "Jonas" eg. "pref1;pref2;;;1;"
                localStorage.setItem(student_name, information[student_name])
            }
            addDict(information, 0, "dropdown", 1); //Add students to dropdown
            information = Object.keys(information); //Add the keys (instead of their values) to list
        }
        addDict(information, 0, list_type, 1);
    });

    request.fail(function(xhr, status, error){
        //alert("Getting " + list_type + "-lists failed! Please reload!" + error.toString()); //TODO: This Error also shows, when new list is created
        console.log("Function getLists failed with ERROR " + error.toString());
    });

    await request;
}

/* Saves the current local Storage into a file */
function saveLocalStorage() {
    //Convert students inside the storage into a string
    var student_str = "";
    for (var i=0; i<localStorage.length; ++i){
        var student = localStorage.key(i);
        if (student === "file_name") {continue;}
        student_str += student + ";" + localStorage.getItem(student) + "|";
    }
    saveData({"name": localStorage.getItem("file_name"), "students": student_str});
}

/* Creates and saves a new element */
function createElement(element_type, name) {
	try {
	    if (name.trim() == "") throw "empty_name"; //Check whether name empty
        switch(element_type) {
            case "class":
                localStorage.clear();
                localStorage.setItem("file_name", name);
                break;
            case "student":
                localStorage.setItem(name, ";;;;;");
                break;
            default:
                throw "unknown_type";
        }
        saveLocalStorage();
        return true;
	} catch (err) {
		switch(err) {
			case 'empty_name':
				err_text = "Name can't be empty"; break;
		    case 'unknown_type':
		        err_text = "Type \"" + element_type + "\" unknown"; break;
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

		showTooltip(element_type + "_tooltip", err_text);
		return false;
	}
}

/*
	Saves changes to student Name and Prefs

	@param name: name of student pre change
*/
function saveStudent() {
	try {
	    //Handle Name --------------------------------
		var old_name = document.getElementById("student_current").innerHTML;
		var new_name = document.getElementById("pref_name").value;
		if(old_name != new_name) {
		    //TODO: Check whether new name is legal
		    localStorage.removeItem(old_name)
		}

        //Handle Prefs ---------------------------
        //TODO: Check whether prefs legal
        pref_string = document.getElementById("pref0").value + ";";
        pref_string += document.getElementById("pref1").value + ";";
        pref_string += document.getElementById("pref2").value + ";";
        pref_string += document.getElementById("pref3").value + ";";
        pref_string += document.querySelector("input[type='radio'][name='position']:checked").value + ";";
		localStorage.setItem(new_name, pref_string);
		saveLocalStorage();
		//TODO: Animation/Tooltip, to show whether it was saved
	} catch(err) {
		switch (err) {
			case "illegal_name":
				//TODO: Handle Error
			default:
				err_text = "Adding student went wrong! Error: " + err; break;
		}
		//TODO: Show tooltip with error message
	}
}