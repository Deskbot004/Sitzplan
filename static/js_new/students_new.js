/*
	This js contains functions called for students_list.html

	Functions:
        loadInformation() - Loads a list (or similar) from the server

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
            document.getElementById('class_name').innerHTML = name;
            break;
        case "pref": //TODO
            var request = requestInformation(name); //TODO: There is no request to get prefs for single student
            document.getElementById('pref_name').value = name;
            break;
        default:
	        alert("students/loadInformation: type \"" + list_type + "\" not recognized");
    }

    request.done( function(information) {
        addDict(information, 0, list_type, 1);
        if (list_type === "student") {addDict(information, 0, "dropdown", 1);}
    });

    request.fail(function(xhr, status, error){
        //alert("Getting " + list_type + "-lists failed! Please reload!" + error.toString()); //TODO: This Error also shows, when new list ist created
        console.log("Function getLists failed with ERROR " + error.toString());
        document.getElementById('pref_name').value = name; //TODO: Remove, once case pref works
    });

    await request;
}