/*
	This js contains all functions used exclusively by seating_list and seating_editor.

	Functions used by seating_list:
		selectElement(event)
		resetBackground(array)
		createInformation()
		async fillLists()
	Functions used by seating_editor:
		start()
*/




//_________________________________Functions used by seating_list______________________________________________




/*
	Overwrites selectElement from listings.js with this function.
	Saves the select element on the right while changing the background of the selected element to yellow.
	The previously selected of the list loses its background color.

	@param event: The event which triggered this function
	@return: void
*/
function selectElement(event) {
    try {
        var parent = event.target.parentNode;
        resetBackground(parent);

        event.target.style.background = "yellow";

        if (parent.id == "stud_list") text = "student";
        if (parent.id == "room_list") text = "classroom";

        var textfield = document.getElementById(text);
        textfield.innerHTML = event.target.innerHTML;
    } catch (err) {
        alert("Selecting element went wrong! The element was not selected!");
        console.log("Function selectElement failed with " + err);
    }

};


/*
	Helper function to remove each background color of a list.

	@return: void
*/
function resetBackground(List) {
    var ul_elements = List.getElementsByTagName('li');
    for (var i = 0, len = ul_elements.length; i < len; i++) {
        ul_elements[i].style.background = "transparent";
    }
};


/*
	Overwrites createInformation from listings.js.
	Creates an array of the relevant information and sends it to seating_editor.

	@param show: Changes the functionality to only show the last one.
	@return: void
*/
function createInformation(show) {
    try {
        var student = document.getElementById("student").innerHTML;
        if (student == "None") throw "student_empty";
        var classroom = document.getElementById("classroom").innerHTML;
        if (classroom == "None") throw "room_empty";
        var algorithm = document.getElementById("algorithm").value;
		if (show == "show") algorithm = "show";

        var data = [student, classroom, algorithm];

        sendInformation(data);
    } catch(err) {
        var err_text = "";
        switch (err) {
            case "student_empty":
                err_text = "Please select a list of students!";
                break;
            case "room_empty":
                err_text = "Please select a classroom!";
                break;
            default: break;
        }

        var popup = document.getElementById("popup")
        if (show == "show") popup = document.getElementById("popup_show")
        popup.innerHTML = err_text;
        popup.classList.toggle("show");
        console.log("Function createInformation() failed with " + err);
    }
};


/*
	Function which on load fills both lists with the existing information.

	@return: void
*/
async function fillLists() {
    identity = "student";
    var stud_list = document.getElementById("stud_list");
    stud_list.id = 'var_list';
    await getLists();
    stud_list.id = "stud_list";

    identity = "classroom";
    var room_list = document.getElementById("room_list");
    room_list.id = "var_list";
    await getLists();
    room_list.id = "room_list";

    identity = "seating";
};




//_________________________________Functions used by seating_list______________________________________________




/*
	Function which on load runs the selected algorithm and displays the created seating.

	TODO

	@return: void
*/
function start() {
	var running_algorithm = requestInformation(data);
};