/*
	This js contains all generic functions for lists of all kinds.

    Functions:
        addElement() - Adds an Element to a list
        addDict() - Adds every Element from a Dictionary into a list
        existsElement() - Checks whether an Element exists in a list
        loadList() - Loads a List from the Server (By calling the load-function from the appropriate js file)

        trimList() - Trims a list down, to only show elements that match the searchbar
        selectElement() - Is called when an Element in the list is clicked
        checkInput() - Checks the input of the create new Element form, for illegal Characters etc. and shows an Error Tooltip when necessary
        createElement() - Creates a new Element for the List (and saves it to the server)

    Common Variables:
        list_id - id of a list
	    list_type - type of a list (see below)

    List-Types:
        "dropdown" - Dropdown menu, that gets narrowed down then you type ("type to search")
        "class" - List of all Classes
        "student" - List of all Students in a Class
*/

//_________________________________Functions________________________________________________

/*
	@param name: String containing the innerHTML of the new Element
	@param remove_duplicates: Boolean if duplicates need to be removed or not
	@return: the added node if successful, 0 otherwise
*/
function addElement(name, remove_duplicates, list_type) {
    var list_id = list_type + "_list";

    //Check for duplicates
    if (remove_duplicates && existsElement(name, list_id)) return 0;

    switch (list_type) {
        case "dropdown": //The list is a dropdown menu, where you can type to narrow it down
            var node = document.createElement('option');
            break;
        default: //The list is a normal ul
            var node = document.createElement('li');
            node.onclick = function(event){selectElement(event.target, list_type);}; //OnClick Function
    }
    node.className += 'elem'; //Class
    node.appendChild(document.createTextNode(name));
    document.getElementById(list_id).appendChild(node);
    return node;
}


/*
    @param element_dict: dictionary containing all Elements to be added
	@param remove_duplicates: Boolean if duplicates need to be removed or not
	@param replace: Boolean, whether the entries already in the list should be replaced (1) or kept (0)
	@return: void
*/
function addDict(element_dict, remove_duplicates, list_type, replace) {
    var list_id = list_type + "_list";
    if (replace) {$("#" + list_id).empty();} //Empty the list first (if replace == 1)
	for (var elem of Object.keys(element_dict)) {
		addElement(element_dict[elem], remove_duplicates, list_type);
	};
}

/*
	@param text: String containing the innerHTML of the Element
	@return: Boolean containing the information if the Element exists
*/
function existsElement(text, list_id) {
    var detected = 0;
    const elem = document.getElementById(list_id);
    var ul_elements = elem.getElementsByTagName('li');
    for (var i = 0, len = ul_elements.length; i < len; i++) {
        if (text == ul_elements[i].innerHTML) {
            detected = 1;
        }
    }
    return detected;
}


function loadList(list_type, name="n/a") {
    loadInformation(list_type, name); //Depends on the .js, that was loaded in the html file
}

//_________________________________Functions from User Interaction________________________________________________

/*
    Trims the list down to only show elements that match the searchbar

    @param searchInput: searchbar object
    @param list_id: Id of the List that should be trimmed
    @return: void
*/
function trimList(searchInput, list_id){
    var searchWord = searchInput.target.value; //Get value inside searchbar
    searchWord = searchWord.trim().toLowerCase(); //Exclude white space and change input to all lowercase

    var fullList = document.getElementById(list_id);
    var result_count = 0;
    for (let elem of fullList.children) {
        if (!elem.innerHTML.trim().toLowerCase().includes(searchWord)) {
            elem.style.display = "none";
        } else {
            document.getElementById(list_id+"_empty").style.display = "none";
            elem.style.display = "block";
            result_count++;
        }
    }

    if (result_count < 1) { //Case no classes were found
        document.getElementById(list_id+"_empty").style.display = "block";
    }
}


/*
	Is called when an Element in a list is clicked

	@param event: The selected element itself
	@param element_type: Same as list_type but for the selected Element
	@return: void
*/
//TODO: hide all popups and clear input fields
function selectElement(event_target, element_type) {
	try {
	    var list_id = element_type + "_list";

	    //Apply .current class to selected item
	    var fullList = document.getElementById(list_id);
	    for (let elem of fullList.children) {
	        elem.classList.remove("current");
	        elem.removeAttribute("id");
	    }
	    event_target.classList.add("current");
	    event_target.id = element_type + "_current";

	    //Determine type of List that should be shown
	    switch (element_type) {
	        case "class":
                var list_type = "student";
                var new_list_id = "student_list";
                break;
            case "student":
                var list_type = "pref";
                var new_list_id = "n/a";
                localStorage.setItem("current_student", event_target.innerHTML);
                break;
            default:
                alert("select Element: type \"" + list_type + "\" unknown"); break;
	    }

	    //Load Information into list
	    loadList(list_type, event_target.innerHTML);
	    //TODO: Currently, the next lines of code don't wait for async function loadList to finish, resulting in a blinking title -> Fix that

	    //Hide Prompt to select an item
        var prompt = document.getElementById(list_type + "_prompt");
        prompt.style.visibility = "hidden";

        //Show the list with selected items
        var hiddenDiv = document.getElementById(list_type + "_container");
        hiddenDiv.style.visibility = "visible";

	} catch (err) {
		alert("Selecting element went wrong! Error: " + err);
		console.log("Function selectElement failed with " + err);
	}
}


/*
    Checks the input of the create new Element form, for illegal Characters etc. and shows an Error Tooltip when necessary

    @param createInput: textinput object
    @param tooltip_id: Id of the tooltip object
    @param list_id: Id of list to check for duplicates
    @return: void
*/
function checkInput(createInput, tooltip_id, list_id, ignore="n/a") {
    var text = createInput.target.value;

    if (!checkForIllegalCharacters(text)) {
        err_text = "The name should only contain letters and numbers!";
        showTooltip(tooltip_id, err_text);
    } else if (existsElement(text, list_id) && text != ignore) {
        err_text = "The entry \"" + text + "\" already exists!";
        showTooltip(tooltip_id, err_text);
    } else {
        hideTooltip(tooltip_id);
    }
}

function showTooltip(tooltip_id, text){
    var tooltip = document.getElementById(tooltip_id);
    tooltip.innerHTML = text;
    tooltip.style.visibility = "visible";
}
//TODO: hide tooltip, when clicking outside if input
function hideTooltip(tooltip_id){
    var tooltip = document.getElementById(tooltip_id);
    tooltip.style.visibility = "hidden";
}


/*
    Is called, when a Create Button is clicked.

    @param tooltip_id: id of the tooltip with the error message, when input is illegal
	@return: void
*/
function createListElement(tooltip_id, input_id, list_type) {
    var tooltip = document.getElementById(tooltip_id);
    if (checkTooltip(tooltip_id)){
        var name = document.getElementById(input_id).value;
        if (!createElement(list_type, name)) return;
        var node = addElement(name, 0, list_type); //Add the new item to list
        selectElement(node, list_type); //Select that new item
        document.getElementById(input_id).value = "";//Clear input field
        event.preventDefault();
        return true;
    }
    return false
}

function checkTooltip(tooltip_id) {
    var tooltip = document.getElementById(tooltip_id);
    if (tooltip.style.visibility == "visible"){ //Name not allowed
        tooltip.style.animation = "1s popupcolor"; //play tooltip animation
        setTimeout(function(){tooltip.style.animation = "";}, 1000); //reset animation
        return false;
    }
    return true;
}