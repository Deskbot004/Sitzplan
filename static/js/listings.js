/*
	This js contains all generic functions for the interactions of "var_list".
	Which is mainly used to show information read by data as a list.


	Functions:
		addElement(string) -> Boolean
		existsElement(string) -> Boolean
		deleteElement(string)
		addList(array)
		addDict(dictionary)
		selectElement(event)
		sendInformation()
	Functions from user interaction:
	    createInformation()
	Requests:
	    getLists()
*/



/*
	Adds given String as List Element to the list with the id "var_list".
	The element gets the class "elem" and the function selectElement(e).

	@param text: String containing the innerHTML of the new Element
	@return: Boolean if adding was successful
*/
function addElement(text) {
    if (existsElement(text)) return 0;
    var node = document.createElement('li');
    node.appendChild(document.createTextNode(text));
    node.className += 'elem';
    node.onclick = function(event){selectElement(event);};
    document.querySelector('#var_list').appendChild(node);
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
        addElement(element_arr[i]);
    };
};

/*
	Executes addElement() for each entry in the given dictionary.

	@param element_dict: dictionary containing all Elements to be added
	@return: void
*/
function addDict(element_dict) {
	for (var elem of Object.keys(element_dict)) {
		addElement(element_dict[elem]);
	};
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
	Takes the information from form called 'filename' and
	executes sendInformation(string) if the information is
	not in 'var_list' yet.

	@return: void
*/
function createInformation() {
    try {
        var text = document.getElementById('filename').value;

        if (!checkForIllegalCharacters(text)) {
            throw "illegal";
        }

        if (existsElement(text)) {
            throw "already_exists";
            var popup = document.getElementById("exists");
            popup.classList.toggle("show");
        }
        sendInformation(text);
    } catch(err) {
        var err_text = "";
        switch (err) {
            case "illegal":
                err_text = "The name should only contain letters and numbers!";
                break;
            case "already_exists":
                err_text = "The entry " + text + " already exists!";
                break;
            default: break;
        }

        var popup = document.getElementById("popup_check")
        popup.innerHTML = err_text;
        popup.classList.toggle("show");
        console.log("Function createInformation() failed with " + err);
    }
};

/*

	Adds every item relevant for the identity as
	a dictionary to 'var_list'.

	@return: void
*/
function getLists() {
    var lists_req = listRequest();
    lists_req.done(function(data) {
        addDict(data);
    });
    lists_req.fail(function(xhr, status, error){
        alert("Getting all lists failed! Please reload!");
		console.log("Function getLists failed with ERROR " + error.toString());
    });
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