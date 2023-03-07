/*
	This js contains functions called by classroom.html.

	Simple functions on html:
		arrayToText(array) -> string
		check_validity(array) -> Boolean
		change_array(array, string, string)
		fillGrid(array, array, string)
	Functions from user interaction:
		changeColor(string)
		addColorClick()
		getInformation(string)
		pre_saveData()
*/




//_________________________________Simple functions on html____________________________________________




/*
    Converts the classroom array into a text string.

	@param classroom: An array of the classroom information
    @return: String of the classroom data
*/
function arrayToText() {
    return classroom.join('-');
};


/*
    Converts the classroom text string into an array.

	@param classroom: String of the classroom data
    @return: An array of the classroom information
*/
function textToArray(room) {
    entries = room.split("-")
    new_room = new Array()
    for (i=0; i < entries.length; i++){
        new_room.push(entries[i].split(","));
    }
    return new_room;
}

/*
    Checks for a valid classroom (at least one teacher and one student desk in the room).

	@param classroom: An array of the classroom information
    @return: Double-digit string describing whether student and teacher desks are present
*/
function check_validity(classroom) {
    var student_found = 0;
    var teacher_found = 0;
    for (i = 0; i < classroom.length; i++) {
        if (classroom[i][2] == "student") student_found = 1;
        if (classroom[i][2] == "teacher") teacher_found = 1;
    }
    return student_found.toString() + teacher_found.toString();
};


/*
    Updates the classroom array with desks.

	@param first_desk: a tuple of coordinates with the position of the first desk
    @param second_desk: a tuple of coordinates with the position of the second desk or Null
    @param type: the type of the desk (either "student", "teacher" or "unusable")
    @return: void
*/
function changeArray(first_desk, second_desk, type) {
	new_entry = new Array();
	new_entry.push(first_desk);
	new_entry.push(second_desk);
	new_entry.push(type);
	classroom.push(new_entry)
};


/*
    Fills the grid with a loaded classroom.

	@param grid: The grid to be coloured
    @param room: String of the loaded classroom
    @return: void
*/
function fillGrid(grid, room) {
    if(room.length <= 0) return;
    // turn the room string into an array
    new_room = textToArray(room);
    teacher_desk_count = 2;
    console.log("FILLING CLASSROOM")
    classroom = new_room;
    for (i = 0; i < new_room.length; i++) {
        switch(new_room[i][2]) {
            case "student":
                document.getElementById(new_room[i][0]).style.backgroundColor = "lightblue";
                if (new_room[i][1] != null) document.getElementById(new_room[i][1]).style.backgroundColor = "lightblue";
                break;
            case "unusable":
                document.getElementById(new_room[i][0]).style.backgroundColor = "orange";
                if (new_room[i][1] != null) document.getElementById(new_room[i][1]).style.backgroundColor = "orange";
                break;
            case "teacher":
                document.getElementById(new_room[i][0]).style.backgroundColor = "pink";
                if (new_room[i][1] != null) document.getElementById(new_room[i][1]).style.backgroundColor = "pink";
                break;
            default: break;
        }
        //changeArray(classroom, grid[num].getAttribute("id"), col_change);
    }
};




//_________________________________Functions from user interaction_____________________________________________




/*
    Changes the color variable that is used to color the background of grid divs.

    @param color_arg: The new color as a string (e.g. "white")
    @return: void
*/
function changeColor(color_arg) {
	try {
		color = color_arg;
	} catch(err) {
		alert("Changing color went wrong! The draw color was not swapped!");
		console.log("Function changeColor failed with " + err);
	}
};

/*
    Clears all grid elements and sets them to white

    @param classroom: An array of the classroom information
	@param grid: The grid to be coloured
    @return: void
*/
function clearAll(grid) {
    try {
        for (num = 0; num < grid.length; num++) {
            grid[num].style.backgroundColor = "white";
            classroom = [];
        }
        teacher_desk_count = 0;
    } catch(err) {
        alert("Something went wrong! Could not clear the grid!");
        console.log("Function clearAll failed with " + err);
    }
};

/*
    Gets the neighbor divs of a cell in the grid

    @param div_id: array containing the cell coordinates
    @return: array with the neighbor divs
*/
function getNeighboringDivColors(div_id) {
    var neighbor_divs = new Array();
    neighbor_divs.push(document.getElementById(String(parseInt(div_id[0]) - 1) + ";" + div_id[1]));
    neighbor_divs.push(document.getElementById(String(parseInt(div_id[0]) + 1) + ";" + div_id[1]));
    neighbor_divs.push(document.getElementById(div_id[0] + ";" + String(parseInt(div_id[1]) - 1)));
    neighbor_divs.push(document.getElementById(div_id[0] + ";" + String(parseInt(div_id[1]) + 1)));
    neighbor_divs = neighbor_divs.filter(function(item) {
        return item !== null
    })
    return neighbor_divs
};

/*
    Highlight the selection in the grid so the user can see which divs a table would be placed on

    @return: void
*/
function highlightSelection() {
    mouse_div = this;
    var div_id = this.getAttribute("id").split(";");
    var highlight_color = "palegreen";
    var error_color = "lightsalmon";
    if (double) {
        if (color != "white") {     // highlight selection for placing desks
            if (orientation == 0) {   // if desk is oriented horizontally
                var neighbor_div = document.getElementById(div_id[0] + ";" + String(parseInt(div_id[1]) + 1));
                if (neighbor_div == null) {
                    this.style.backgroundColor = error_color;
                    return;
                }
                if (this.style.backgroundColor == "white" && neighbor_div.style.backgroundColor == "white") {
                    this.style.backgroundColor = highlight_color;
                    neighbor_div.style.backgroundColor = highlight_color;
                } else if (this.style.backgroundColor == "white" && neighbor_div.style.backgroundColor != "white") {
                    this.style.backgroundColor = error_color;
                }
            } else {    // if desk is oriented vertically
                var neighbor_div = document.getElementById(String(parseInt(div_id[0]) - 1) + ";" + div_id[1]);
                if (neighbor_div == null) {
                    this.style.backgroundColor = error_color;
                    return;
                }
                if (this.style.backgroundColor == "white" && neighbor_div.style.backgroundColor == "white") {
                    this.style.backgroundColor = highlight_color;
                    neighbor_div.style.backgroundColor = highlight_color;
                } else if (this.style.backgroundColor == "white" && neighbor_div.style.backgroundColor != "white") {
                    this.style.backgroundColor = error_color;
                }
            }
        } else {    // highlight selection for removing desks
            coordinate = String(div_id[0] + ";" + div_id[1]);
            desk_coord = searchArray(classroom, coordinate);
            if (desk_coord.length == 0)  {
                this.style.backgroundColor = error_color;
            } else {
                for (i = 0; i < desk_coord.length - 1; i++) {
                    document.getElementById(desk_coord[i]).style.backgroundColor = highlight_color;
                }
            }
        }
    }
}

/*
    Searches a classroom array for an entry that matches the given coordinate and returns all coordinates belonging
    to that entry

    @param classroom: the array to be searched
    @param coord: the coordinate to be checked

    @return: the coordinates of the found entry (can be emtpy)
*/
function searchArray(classroom, coord) {
    for (i = 0; i < classroom.length; i++) {
        for (j = 0; j < classroom[i].length; j++) {
            if (classroom[i][j] == coord) return classroom[i];
        }
    }
    return []
}

/*
    Rotate the selection of a double desk on the grid and change where the desk would be placed

    @param e: the key pressed (has to be "r")
    @return: void
*/
function rotate(e) {
    if(window.event) { // IE
    keynum = e.keyCode;
    } else if(e.which){ // Netscape/Firefox/Opera
    keynum = e.which;
    }
    var highlight_color = "palegreen";
    var error_color = "lightsalmon";

    if (keynum == 114 && double) { // rotate when "r" key is pressed
        if (mouse_div != null) {
            var div_id = mouse_div.getAttribute("id").split(";");
            if (orientation == 0) {     // if table is oriented horizontally
                old_neighbor = document.getElementById(div_id[0] + ";" + String(parseInt(div_id[1]) + 1));
                new_neighbor = document.getElementById(String(parseInt(div_id[0]) - 1) + ";" + div_id[1]);
            } else {        // if table is oriented vertically
                old_neighbor = document.getElementById(String(parseInt(div_id[0]) - 1) + ";" + div_id[1]);
                new_neighbor = document.getElementById(div_id[0] + ";" + String(parseInt(div_id[1]) + 1));
            }
            if (mouse_div.style.backgroundColor == highlight_color) {
                if (new_neighbor != null) {
                    if (new_neighbor.style.backgroundColor == "white") {
                        old_neighbor.style.backgroundColor = "white";
                        new_neighbor.style.backgroundColor = highlight_color;
                    } else {
                        old_neighbor.style.backgroundColor = "white";
                        mouse_div.style.backgroundColor = error_color;
                    }
                } else {
                    if (old_neighbor != null) old_neighbor.style.backgroundColor = "white";
                    mouse_div.style.backgroundColor = error_color;
                }
            } else if (mouse_div.style.backgroundColor == error_color && old_neighbor != null) {
                if (new_neighbor != null) {
                    if (new_neighbor.style.backgroundColor == "white") {
                        mouse_div.style.backgroundColor = highlight_color;
                        new_neighbor.style.backgroundColor = highlight_color;
                    } else {
                        mouse_div.style.backgroundColor = error_color;
                    }
                } else {
                    if (old_neighbor != null) old_neighbor.style.backgroundColor = "white";
                    mouse_div.style.backgroundColor = error_color;
                }
            }
        }
        orientation = Math.abs(orientation - 1);
    }
}
/*
    Deselects the highlight selection on the grid if the mouse cursor is moved out of a cell

    @return: void
*/

function highlightDeselection() {
    var div_id = this.getAttribute("id").split(";");
    var highlight_color = "palegreen";
    var error_color = "lightsalmon";
    if (double) {
        if (color != "white") {     // highlight deselection for empty spaces
            if (orientation == 0) {   // if table is oriented horizontally
                var neighbor_div = document.getElementById(div_id[0] + ";" + String(parseInt(div_id[1]) + 1));
                if (this.style.backgroundColor == error_color) this.style.backgroundColor = "white";
                if (neighbor_div == null) return;
                if (this.style.backgroundColor == highlight_color && neighbor_div.style.backgroundColor == highlight_color) {
                    this.style.backgroundColor = "white";
                    neighbor_div.style.backgroundColor = "white";
                }
            } else {    // if table is oriented vertically
                var neighbor_div = document.getElementById(String(parseInt(div_id[0]) - 1) + ";" + div_id[1]);
                if (this.style.backgroundColor == error_color) this.style.backgroundColor = "white";
                if (neighbor_div == null) return;
                if (this.style.backgroundColor == highlight_color && neighbor_div.style.backgroundColor == highlight_color) {
                    this.style.backgroundColor = "white";
                    neighbor_div.style.backgroundColor = "white";
                }
            }
        } else {    // highlight deselection for desks
            coordinate = String(div_id[0] + ";" + div_id[1]);
            desks = searchArray(classroom, coordinate);
            if (desks.length == 0) {
                this.style.backgroundColor = "white";
            } else {
                desk_type = desks[desks.length - 1];
                desk_coord = desks.slice(0, -1);
                switch (desk_type) {
                    case "student":
                        new_color = "lightblue";
                        break;
                    case "teacher":
                        new_color = "pink";
                        break;
                    case "unusable":
                        new_color = "orange";
                        break;
                     default:
                        new_color = "black";
                        console.log("WRONG DESK_TYPE");
                }
                for (i = 0; i < desk_coord.length; i++) {
                    document.getElementById(desk_coord[i]).style.backgroundColor = new_color;
                }
            }
        }
    }
}

/*
    Changes the background color of a grid cell.

    @return: void
*/
function addColorClick() {
	try {
	    var highlight_color = "palegreen";
        var error_color = "lightsalmon";
        var div_id = this.getAttribute("id").split(";");
        if (this.style.backgroundColor == highlight_color) {
            if (orientation == 0) {     // if table is oriented horizontally
                neighbor = document.getElementById(div_id[0] + ";" + String(parseInt(div_id[1]) + 1));
            } else {        // if table is oriented vertically
                neighbor = document.getElementById(String(parseInt(div_id[0]) - 1) + ";" + div_id[1]);
            }
            if (color != "pink") {
                if (this.style.backgroundColor == "pink") teacher_desk_count -= 1;
                this.style.backgroundColor = color;
                neighbor.style.backgroundColor = color;
                if (color == "lightblue") changeArray(this.getAttribute("id"), neighbor.getAttribute("id"), "student");
                if (color == "orange") changeArray(this.getAttribute("id"), neighbor.getAttribute("id"), "unusable");
            } else {
                switch (teacher_desk_count) {
                    case 0:
                        this.style.backgroundColor = color;
                        neighbor.style.backgroundColor = color;
                        changeArray(this.getAttribute("id"), neighbor.getAttribute("id"), "teacher");
                        teacher_desk_count += 1;
                        break;
                    case 1:
                    case 2:
                        throw "desk limit";
                        break;
                    default:
                        console.log("teacher_desk_count is " + String(teacher_desk_count) +
                        "! Something went REALLY wrong!");
                        break;
                }
            }
        }
        console.log(classroom)
    } catch(err) {
        err_text = "Unknown Error!"
        console.log(err)
		switch (err) {
	        case "no neighbor":
	            err_text = "No neighboring teacher desk!";
	            break;
	        case "desk limit":
	            err_text = "The maximum number of teacher desks has been reached!";
	            break;
	        default:
                console.log("teacher_desk_count is " + String(teacher_desk_count) +
                "! Something went REALLY wrong!");
                break;
	    }
	    var popup = document.getElementById("popup_teacher");
		popup.innerHTML = err_text;
		popup.classList.toggle("show");

		switch(typeof err) {
			case "string":
				console.log("Function addColor failed with " + err);break;
			case "object":
				console.log("Adding color failed with "+ err);
				console.log(err);
				break;
			default:
				console.log("Undetected Error type: " + typeof err);break;
		}
    }
};


/*
    Loads the information of a given classroom

    @return: void
*/
function getInformation(text){
	try {
		var req_room = requestInformation(text);
		req_room.done(function(room) {
			fillGrid(grid, room);
		});
		req_room.fail(function() {
			console.log("No file named "+ text + " found, loading template.");
			classroom = [["7;7", "7;8", "student"], ["8;7", "8;8", "teacher"]]
			room = "7;7,7;8,student-8;7,8;8,teacher"
			fillGrid(grid, room);
		});
	} catch(err) {
		alert("Getting Information went wrong! The room was not properly loaded!");
		console.log("Function getInformation failed with " + err);
		popup.classList.toggle("show");
	}
};


/*
	Function to test specific edge cases before sending the information to generic saveData().

	@return: void
*/
function pre_saveData() {
	try {
		var error_case = "Not request fail";
		switch (check_validity(classroom)) {
	        case "00":
	            throw "no_student_or_teacher";
	        case "01":
	            throw "no_student";
	        case "10":
	            throw "no_teacher";
	        default: break;
	    }

	    var layout_array = arrayToText(classroom);
	    var name = document.getElementById("filename").value;

	    saveData({"name" : name, "layout": layout_array});
	} catch (err) {
		switch(err) {
			case 'no_student_or_teacher':
				err_text = "Your classroom needs at least one student and one teacher desk!"; break;
			case 'no_student':
				err_text = "Your classroom needs at least one student desk!"; break;
			case 'no_teacher':
				err_text = "Your classroom needs at least one teacher desk!"; break;
			default:
				err_text = "Saving classroom went wrong! The room has not been saved!"; break;
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