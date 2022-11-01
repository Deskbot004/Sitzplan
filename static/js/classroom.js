/*
	This js contains functions called by classroom.html.

	Simple functions on html:
		arrayToText(array) -> string
		detectWidthToTrim(array) -> array
		detectHeightToTrim(array) -> array
		check_validity(array) -> Boolean
		change_array(array, string, string)
		fillGrid(array, array, string)
	Functions from user interaction:
		changeColor(string)
		addColor()
		addColorClick()
		getInformation(string)
		pre_saveData()
*/




//_________________________________Simple functions on html____________________________________________




/*
    Converts the classroom array into a text string where the rows are separated by semicolons.

	@param classroom: An array of the classroom information
    @return: String of the classroom data
*/
function arrayToText(classroom) {
    var width = detectWidthToTrim(classroom);
    var height = detectHeightToTrim(classroom);
    var place_semi = 0;
    var text = "";
    var text_untrimmed = "";

    for (let x = 0; x < grid_height; x++) {
        place_semi = 0;
        for (let y = 0; y < grid_length; y++) {
            text_untrimmed += classroom[x][y].toString();
            if (width[0] <= y && y <= width[1] && height[0] <= x && x <= height[1]) {
                text += classroom[x][y].toString();
                place_semi = 1;
            }
        }
        text_untrimmed += ";";
        if (place_semi) text += ";";
    }
    var text_array = [text, text_untrimmed];
    return text_array;
};


/*
    Detects if columns can be trimmed (are only filled with zeros) from the array representing the classroom data.

	@param classroom: An array of the classroom information
    @return: List with two entries describing the interval of columns that can't be trimmed
*/
function detectWidthToTrim(classroom) {
    var start_width = 99;
    var end_width = 0;
    var found_num = 0;
    var entry = 0;

    for (let x = 0; x < grid_height; x++) {
        found_num = 0;
        for (let y = 0; y < grid_length; y++) {
            entry = classroom[x][y];
            if (entry != 0 && found_num == 0) {
                found_num = 1;
                if (y < start_width) start_width = y;
            } else if (entry != 0) {
                if (y > end_width) end_width = y;
            }
        }
    }
    return [start_width, end_width];
};


/*
    Detects if rows can be trimmed (are only filled with zeros) from the array representing the classroom data.

	@param classroom: An array of the classroom information
    @return: List with two entries describing the interval of columns that can't be trimmed
*/
function detectHeightToTrim(classroom) {
    var start_height = 99;
    var end_height = 0;
    var found_num = 0;

    for (let x = 0; x < grid_height; x++) {
        found_num = 0;
        for (let y = 0; y < grid_length; y++) {
            if (classroom[x][y] != 0) found_num = 1;
        }
        if (found_num == 1) {
            if (x < start_height) start_height = x;
            if (x > end_height) end_height = x;
        }
    }

    return [start_height, end_height];
};


/*
    Checks for a valid classroom (at least one teacher and one student desk in the room).

	@param classroom: An array of the classroom information
    @return: Double-digit string describing whether student and teacher desks are present
*/
function check_validity(classroom) {
    var student_found = 0;
    var teacher_found = 0;
    for (let x = 0; x < grid_height; x++) {
        found_num = 0;
        for (let y = 0; y < grid_length; y++) {
            if (classroom[x][y] == 1) student_found = 1;
            if (classroom[x][y] == 3) teacher_found = 1;
        }
    }
    return student_found.toString() + teacher_found.toString();
};


/*
    Updates the classroom array with new color values.

	@param classroom: An array of the classroom information
    @param array_id: The array entry that is to be changed as a double-digit string
    @param color: The new color as a string (e.g. "white")
    @return: void
*/
function changeArray(classroom, array_id, color) {
    var x_val = array_id[0];
    var y_val = array_id[1];
    switch(color) {
        case "white":
            classroom[x_val][y_val] = 0;
            break;
        case "lightblue":
            classroom[x_val][y_val] = 1;
            break;
        case "orange":
            classroom[x_val][y_val] = 2;
            break;
        case "pink":
            classroom[x_val][y_val] = 3;
            break;
        default:
    }
};


/*
    Fills the grid with a loaded classroom.

	@param classroom: An array of the classroom information
	@param grid: The grid to be coloured
    @param room: String of the loaded classroom
    @return: void
*/
function fillGrid(classroom, grid, room) {
    if(room.length <= 0) return;
    var room = room.replace(/;/g, "");
    var col_change = "";

    for (num = 0; num < room.length; num++) {
        switch(room[num]) {
            case "0":
                col_change = "white";
                break;
            case "1":
                col_change = "lightblue";
                break;
            case "2":
                col_change = "orange";
                break;
            case "3":
                col_change = "pink";
                break;
            default: break;
        }
        grid[num].style.backgroundColor = col_change;
        changeArray(classroom, grid[num].getAttribute("id"), col_change);
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
    Changes the background color of a grid div upon downward press of the left mouse button.

    @return: void
*/
function addColor() {
	try {
	    if (window.mouseDown) {
	        this.style.backgroundColor = color;
	        var div_id = this.getAttribute("id");
	        changeArray(classroom, div_id, color);
	    }
	} catch(err) {
		alert("Adding color went wrong! The color was not correctly applied!");
		console.log("Function addColor failed with " + err);
	}
};


/*
    Changes the background color of a grid.

    @return: void
*/
function addColorClick() {
	try {
        this.style.backgroundColor = color;
        var div_id = this.getAttribute("id");
        changeArray(classroom, div_id, color);
    } catch(err) {
		alert("Adding color went wrong! The color was not correctly applied!");
		console.log("Function addColorClick failed with " + err);
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
			fillGrid(classroom, grid, room);
		});
		req_room.fail(function() {
			console.log("No file named "+ text + " found, loading template.");
			room = "000000000000000;000000000000000;000000000000000;000000000000000;000000000000000;000000000000000;000000011000000;000000011000000;000000033000000;000000000000000;000000000000000;000000000000000;000000000000000;000000000000000;000000000000000;";
			fillGrid(classroom, grid, room);
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

	    saveData({"name" : name, "layout": layout_array[0], "layout_untrimmed": layout_array[1]});
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