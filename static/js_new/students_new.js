/*
	This js contains functions called for students_list.html

	Functions:
        loadInformation() - Loads a list (or similar) from the server
        saveLocalStorage() - Saves current local Storage into a file
        createElement() - Creates a new class/student
        resetPrefs() - Resets the local information about an input field
        checkPrefs() - Reads pref input and shows tooltip on illegal argument/saves changes locally on legal argument
        addPrefField() - Shows corresponding pref input field, when clicking on a pref button
        saveStudent() - Saves student to the server

    Common Variables:
        list_id - id of a list
	    list_type - type of a list (see below)

    List-Types:
        "dropdown" - Dropdown menu, that gets narrowed down then you type ("type to search")
        "class" - List of all Classes
        "student" - List of all Students in a Class
        "pref" - Preferences of a single student
*/

//_________________________________Functions________________________________________________
//TODO: Preferences wird nicht geschlossen, wenn man ne neue klasse öffnet
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
            //Hide student from dropdown table

            //Load Prefs
            var prefs = localStorage.getItem(name).split(";");

            //Input Prefs into corresponding text field
            document.getElementById('pref_name').value = name;
            document.getElementById('pref0').value = prefs[0];
            document.getElementById('pref1').value = prefs[1];
            document.getElementById('pref2').value = prefs[2];
            document.getElementById('pref3').value = prefs[3];

            //Save them to local Storage and disable their entries
            localStorage.setItem("pref_0", prefs[0]);
            localStorage.setItem("pref_1", prefs[1]);
            localStorage.setItem("pref_2", prefs[2]);
            localStorage.setItem("pref_3", prefs[3]);
            updateDropdown();

            //Make pref1 and pref2 visible/invisible, depending on whether they have a value
            var prefButton = 0;
            for(var i=0; i<4; i++){
                if(prefs[i]){togglePref(i, "none", "block");}
                else if(!prefButton || i==3){togglePref(i, "block", "none"); prefButton=1;}
                else{togglePref(i, "none", "none");}
            }

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
            information = Object.keys(information); //Add the keys (instead of their values) to list
            addDict(information, 0, "dropdown", 1); //Add students to dropdown
        }
        addDict(information, 0, list_type, 1);
    });

    request.fail(function(xhr, status, error){
        //alert("Getting " + list_type + "-lists failed! Please reload!" + error.toString()); //TODO: This Error also shows, when new list is created
        console.log("Function getLists failed with ERROR " + error.toString());
    });

    await request;
}

/*
    Saves the current local Storage into a file. Ignores keys in it, that contain "_"
*/
function saveLocalStorage() {
    //Convert students inside the storage into a string
    var student_str = "";
    for (var i=0; i<localStorage.length; ++i){
        var student = localStorage.key(i);
        if (student.includes('_')) {continue;}
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

//_________________________________Handling Prefs________________________________________________
/*
    Turns Element of a pref on/off
    @param pref_nr: Nr of pref (between 0 and 3)
    @param button_display: display style of button ("none" or "block")
    @param form_display: display style of form ("none" or "block")
*/
function togglePref(pref_nr, button_display, form_display){
    document.getElementById("pref"+pref_nr+"_button").style.display = button_display;
    document.getElementById("pref"+pref_nr+"_form").style.display = form_display;
}

/*
    Removes a Pref field and ripples the other fields
*/
function removePref(pref_nr){
    if(pref_nr >= 2){ //Last pref in list
        document.getElementById("pref"+pref_nr).value = "";
        localStorage.removeItem("pref_" + pref_nr);
        togglePref(pref_nr, "block", "none");
    }else{
        var next_pref = document.getElementById("pref"+(pref_nr+1)+"_form");
        if(next_pref.style.display!="none"){ //Next Pref has a value
            document.getElementById("pref"+pref_nr).value = document.getElementById("pref"+(pref_nr+1)).value;
            localStorage.setItem("pref_" + pref_nr, document.getElementById("pref"+pref_nr).value);
            removePref(pref_nr+1);
        }else{ //Next pref is empty
            document.getElementById("pref"+pref_nr).value = "";
            localStorage.removeItem("pref_" + pref_nr);
            togglePref(pref_nr, "block", "none");
            for(var i=pref_nr+1; i<3; i++){
                togglePref(i, "none", "none");
            }
        }
    }
    updateDropdown();
}

/*
    Updates the dropdown for the prefs input fields (meaning removes used students/adds unused students),
    based on information from the local storage
*/
function updateDropdown(){
    disableEntry(localStorage.getItem("current_student"), "dropdown_list", 1);
    for(var i=0; i<4; i++){
        disableEntry(localStorage.getItem("pref_"+i), "dropdown_list", 0);
    }
}

/*
    Should be called when input field is focused
*/
function resetPref(pref_nr) {
    hideTooltip('pref' + pref_nr + '_tooltip');
    localStorage.removeItem("pref_" + pref_nr);
    updateDropdown();
}

function checkPref(pref_nr) {
    var pref_id = "pref" + pref_nr;
    var pref = document.getElementById(pref_id);
    updateDropdown();
    var dropdown = document.getElementById("dropdown_list");

    try {
        if (pref.value.trim() == "") {throw "empty_field";} //Field Empty
        for (let student of dropdown.children) { //Find Element in dropdown list that matches input
            if(pref.value == student.innerHTML) {
                if(student.disabled) {throw "student_used";} //Student was already used elsewhere
                else { //Legal selection
                    localStorage.setItem("pref_" + pref_nr, pref.value);
                    updateDropdown();
                    return true;
                }
            }
        }
        throw "not_student";
        return true;
    } catch(err) {
        switch(err) {
            case "empty_field":
                err_text = "Please enter student or delete field"; break;
            case "student_used":
                err_text = "Student already used"; break;
            case "not_student":
                err_text = "Student \"" + pref.value + "\" not found"; break;
            default:
                err_text = "Error: " + err;
        }
        showTooltip(pref_id + "_tooltip", err_text);
        return false;
    }
}



function addPrefField(pref_nr){
    document.getElementById("pref"+pref_nr+"_button").style.display = "none";
    document.getElementById("pref"+pref_nr+"_form").style.display="block";
    //TODO: Focus on new field
    //$(pref_id + " input").focus();
}

//_________________________________Unsorted Functions________________________________________________

/*
	Saves changes to student Name and Prefs

	@param name: name of student pre change
*/
function saveStudent() {
	try {
	    //Handle Name --------------------------------
		var old_name = document.getElementById("student_current").innerHTML; //TODO: Evt braucht man die student_current-id wg local storage nicht
		var new_name = document.getElementById("pref_name").value;
		if(old_name != new_name) {
		    if(!checkTooltip("pref_name_tooltip")) {return false;}
		    if (new_name.trim() == "") {showTooltip("pref_name_tooltip", "Name can't be empty"); return false;}
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

		//Save everything
		saveLocalStorage();
		document.getElementById("student_current").innerHTML = new_name;
		alert("Saved"); //TODO: Animation/Tooltip, to show whether it was saved
	} catch(err) {
	    alert("Error: " + err);
	}
}

function openRename() {
    document.getElementById("class_name").style.display = "none";
    document.getElementById("class_name_input").value = document.getElementById("class_name").innerHTML;
    document.getElementById("class_name_input").style.display = "block";
    document.getElementById("class_name_input").focus();
}

async function renameClass() {
    if(!checkTooltip("class_name_tooltip")) {return false;}

    //Rename File#
    var old_name = localStorage.getItem("file_name");
    var new_name = document.getElementById("class_name_input").value;
    await renaming(old_name, new_name);
    localStorage.setItem("file_name", new_name);
    saveLocalStorage();

    //Change input to title
    document.getElementById("class_name_input").style.display = "none";
    document.getElementById("class_name").innerHTML = document.getElementById("class_name_input").value;
    document.getElementById("class_name").style.display = "block";

    //Change name in class list
    loadInformation("class", "class_list");
}