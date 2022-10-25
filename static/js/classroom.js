/*
	This js contains functions called by classroom.html.

	Functions:
		arrayToText(array) -> string
		detectWidthToTrim(array) -> array
		detectHeightToTrim(array) -> array
		check_validity(array) -> Boolean
		change_array(array, string, string)
		fillGrid(array, array, string)
		changeColor(string)
		addColor()
		addColorClick()
		sendClassroomToFlask()
		renaming(string, string) -> Boolean
		existsElement(string)
		getInformation(string)
		deleteInformation()
*/



/*
    Converts the classroom array into a text string where the rows are separated by semicolons.

	@param classroom: An array of the classroom information
    @return: string of the classroom data
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
    @return: list with two entries describing the interval of columns that can't be trimmed
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
    @return: list with two entries describing the interval of columns that can't be trimmed
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
    @return: double-digit string describing whether student and teacher desks are present
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
	@param grid: the grid to be coloured
    @param room: string of the loaded classroom
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

/*
    Changes the color variable that is used to color the background of grid divs.

    @param color_arg: The new color as a string (e.g. "white")
    @return: void
*/
function changeColor(color_arg) { color = color_arg; };

/*
    Changes the background color of a grid div upon downward press of the left mouse button.

    @return: void
*/
function addColor() {
    if (window.mouseDown) {
        this.style.backgroundColor = color;
        var div_id = this.getAttribute("id");
        changeArray(classroom, div_id, color);
    }
};

/*
    Changes the background color of a grid.

    @return: void
*/
function addColorClick() {
    this.style.backgroundColor = color;
    var div_id = this.getAttribute("id");
    changeArray(classroom, div_id, color);
};

/*
    Sends the string representing the classroom data to the server.

    @return: void
*/
async function sendClassroomToFlask() {
    switch (check_validity(classroom)) {
        case "00":
            var popup = document.getElementById("no_student_or_teacher");
            popup.classList.toggle("show");
            return
        case "01":
            var popup = document.getElementById("no_student");
            popup.classList.toggle("show");
            return
        case "10":
            var popup = document.getElementById("no_teacher");
            popup.classList.toggle("show");
            return
        default: break;
    }


    var name = document.getElementById("filename").value;
    var layout_array = arrayToText(classroom);

    if (!checkForIllegalCharacters(name)) {
        var popup = document.getElementById("illegal");
        popup.classList.toggle("show");
        return
    }

    rename_value = await renaming(data, name);
	if (name != data) {
		if(!rename_value) return;
	}

	var popup = document.getElementById("saved");
	popup.classList.toggle("show");

	data = name;

    $.post("/classroom_info", {"name" : name, "layout": layout_array[0], "layout_untrimmed": layout_array[1]})
        .done(function(data) {})
        .fail(function(xhr, status, error) {
            console.log("ERROR");
        });
};

/*
	Function that renames a classroom if the name does not already exist.

	@param old_name: Old name of the classroom as String
	@param new_name: New name of the classroom as String
	@return: Boolean if successful or not
*/
async function renaming(old_name, new_name) {
    var rename_return = 0;
    var data_dict = await renameRequest();
    var new_name_exists = 0;
    for (var elem of Object.keys(data_dict)) {
        if(data_dict[elem] == new_name) {
            new_name_exists = 1;
        }
    }

    var old_name_exists = 0;
    for (var elem of Object.keys(data_dict)) {
        if(data_dict[elem] == old_name) {
            old_name_exists = 1;
        }
    }

    if (new_name_exists) {
        var popup = document.getElementById("exists");
        popup.innerHTML = popup.innerHTML.replace("free", new_name);
        popup.classList.toggle("show");
        return 0;
    }

    localStorage.removeItem("exists");
    document.getElementById('head_text').innerHTML = document.getElementById('head_text').innerHTML.replace(old_name, new_name);
    if (old_name_exists) {
        $.post("/delclassroom", { "result": old_name }, function(old_data) {});
    }

    return 1;
};

/*
	Function to see if a classroom name already exists in data.

	@param text: Name of the classroom
	@return: void
*/
function renameRequest() {
    return $.ajax({
		type: "GET",
		url: "/getclassroomlists"
	});

}

/*
    Fill grid with information if a classroom is loaded from the server.

    @param text: string of the classroom name
    @return: void
*/
function getInformation(text){
    $.post("/getclassroomlists", {"result": text}, function(data) {fillGrid(classroom, grid, data);});
};

/*
    Deletes the current classroom from the server.

    @return: void
*/
function deleteInformation() {
	$.post("/delclassroom", { "result": data }, function(data) {switchToClassroom();});
};