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
//TODO: Local storage dictionary variable "read_dictionary"
async function loadInformation(list_type, name) {
    var list_id = list_type + "_list";

    switch (list_type) {
        case "class":
            var request = listRequest();
            break;
        case "student":
            var request = requestInformation(name);
            document.getElementById('class_name').innerHTML = name;
            break;
        case "pref": //TODO
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
                default: //checked="checked"
                    document.getElementById('Either').checked = "checked";
            }
            break;
        default:
	        alert("students/loadInformation: type \"" + list_type + "\" not recognized");
    }

    request.done( function(information) {
        if (list_type === "student") {  //TODO: needs a small rework to fit the new format of classes rn preferences get loaded instead
            //Save student prefs to local Storage
            localStorage.clear();
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
        document.getElementById('pref_name').value = name; //TODO: Remove, once case pref works
    });

    await request;
}


function saveElement(element_type, name) {
	try {
	    //Check whether name empty
	    if (name.trim() == "") throw "empty_name";

        if (element_type == "class") {
            var title = name;
            var student_str = "";
        } else if (element_type == "student") {
            var title = document.getElementById('class_name').innerHTML;
            var student_str = "";

            //list to str
            var list = document.getElementById("student_list");
            var elements = list.getElementsByTagName("li");
            for ( var i = 0, len = elements.length; i < len; i++) {
                student_str += elements[i].innerHTML + "|"; //TODO: hier die prefs hinzufügen
            }
            student_str += name + "|";
        }
        saveData({"name": title, "students": student_str});
        //TODO update preflists when everything went fine
        return true;
	} catch (err) {
		switch(err) {
			case 'empty_name':
				err_text = "Name can't be empty"; break;
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