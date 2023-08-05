/*
	This js contains all generic functions for the interactions of "var_list".
	Which is mainly used to show information read by data as a list.


	Functions:
		addElement(string) -> Boolean
		existsElement(string) -> Boolean
		deleteElement(string)
		addList(array)
		addDict(dictionary)
		getLists()
		sendInformation()
	Functions from user interaction:
	    createInformation()
	    selectElement(event)
	    searchList(event)
	    errorPopup(event)
*/


//_________________________________Functions________________________________________________




/*
	Adds given String as List Element to the list with the id "var_list".
	The element gets the class "elem" and the function selectElement(e).

	@param text: String containing the innerHTML of the new Element
	@param remove_duplicates: Boolean if duplicates need to be removed or not
	@return: Boolean if adding was successful
*/
function addElement(text, remove_duplicates) {
    if (remove_duplicates && existsElement(text)) return 0;
    var node = document.createElement('li');
    node.appendChild(document.createTextNode(text));
    node.className += 'elem';
    node.onclick = function(event){selectElement(event);};
    document.getElementById("var_list").appendChild(node);
    return 1;
};


/*
	Checks the List named "var_list" if it contains an Element with
	the given text as its innerHTML.

	@param text: String containing the innerHTML of the Element
	@return: Boolean containing the information if the Element exists
*/
function existsElement(text) {
    var detected = 0;
    const elem = document.getElementById('var_list');
    var ul_elements = elem.getElementsByTagName('li');
    for (var i = 0, len = ul_elements.length; i < len; i++) {
        if (text == ul_elements[i].innerHTML) {
            detected = 1;
        }
    }
    return detected;
};


/*
	Deletes the list entry containing the given string as its innerHTML
	from the list with the id "var_list".

	@param text: String containing the innerHTML of the Element
	@return: void
*/
function deleteElement(text) {
    const elem = document.getElementById('var_list');
    var ul_elements = elem.getElementsByTagName('li');
    for (var i = 0, len = ul_elements.length; i < len; i++) {
        if (text == ul_elements[i].innerHTML) {
            elem.removeChild(ul_elements[i]);
            return;
        }
    }
};


/*
	Executes addElement() for each entry in the given array.

	@param element_arr: Array containing all Elements to be added
	@return: void
*/
function addList(element_arr) {
    for (var i = 0; i < element_arr.length; i++) {
        addElement(element_arr[i], 1);
    };
};


/*
	Executes addElement() for each entry in the given dictionary.

	@param element_dict: dictionary containing all Elements to be added
	@param remove_duplicates: Boolean if duplicates need to be removed or not
	@return: void
*/
function addDict(element_dict, remove_duplicates) {
	for (var elem of Object.keys(element_dict)) {
		addElement(element_dict[elem], remove_duplicates);
	};
};


/*

	Adds every item relevant for the identity as
	a dictionary to 'var_list'.

	@return: void
*/
function getLists() {
    var lists_req = listRequest();
    lists_req.done(function(data) {
        addDict(data, 1);
    });
    lists_req.fail(function(xhr, status, error){
        alert("Getting all lists failed! Please reload!");
		console.log("Function getLists failed with ERROR " + error.toString());
    });
    return listRequest();
};


/*
	Retains the selected Information and relocates
	to the next relevant site depending on identity.

	@return: void
*/
function sendInformation(text){
    localStorage.setItem('selected', text);
    window.location = "/from_" + identity;
}




//_________________________________Functions from user interaction_______________________________________




/*
	Takes the information from form called 'filename' and
	executes sendInformation(string) if the information is
	not in 'var_list' yet.

	@return: void
*/
function createInformation() {
    var popup = document.getElementById("popup_check")
    if (popup.style.visibility == "visible"){
        popup.style.animation = "1s popupcolor"; //play popup animation
        setTimeout(function(){popup.style.animation = "";}, 1000); //reset animation
        //console.log("Function createInformation() failed with " + err);
        return false;
    } else {
        var text = document.getElementById('filename').value;
        sendInformation(text);
        event.preventDefault();
    }
};


/*
	Executes sendInformation for the selected Element.

	@param event: The selected element itself
	@return: void
*/
function selectElement(event) {
	try {
		sendInformation(event.target.innerHTML);
	} catch (err) {
		alert("Selecting element went wrong! The element was not selected!");
		console.log("Function selectElement failed with " + err);
	}
};


/*
    Trims the list down to only show elements that match the searchbar

    @param searchInput: searchbar object
    @return: void
*/
function searchList(searchInput){
    //Get value inside searchbar
    let searchWord = searchInput.target.value;
    //Exclude white space and change input to all lowercase
    searchWord = searchWord.trim().toLowerCase();

    let fullList = document.getElementById("var_list");
    for (let elem of fullList.children) {
        if (!elem.innerHTML.trim().toLowerCase().includes(searchWord)) {
            elem.style.display = "none";
        } else {
            elem.style.display = "block";
        }
    }
};


/*
    Creates a Popup Bubble with error message when entering wrong input

    @param createInput: textinput object
    @return: void
*/
function errorPopup(createInput) {
    var text = createInput.target.value;
    var popup = document.getElementById("popup_check");

    if (!checkForIllegalCharacters(text)) {
        err_text = "The name should only contain letters and numbers!";
        popup.innerHTML = err_text;
        popup.style.visibility = "visible";
    } else if (existsElement(text)) {
        err_text = "The entry \"" + text + "\" already exists!";
        popup.innerHTML = err_text;
        popup.style.visibility = "visible";
    } else {
        popup.style.visibility = "hidden";
    }
}