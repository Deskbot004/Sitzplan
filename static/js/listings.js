/*
	Adds given String as Element to the shown list




*/
function addElement(text) {
    if (existsElement(text)) return;
    var node = document.createElement('li');
    node.appendChild(document.createTextNode(text));
    node.className += 'elem';
    node.onclick = function(event){selectElement(event);};
    document.querySelector('#var_list').appendChild(node);
}

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
}

/* Deletes Entry from list !!Does not delete in data yet!! */
function deleteElement(text) {
    const elem = document.getElementById('var_list');
    var ul_elements = elem.getElementsByTagName('li');
    for (var i = 0, len = ul_elements.length; i < len; i++) {
        if (text == ul_elements[i].innerHTML) {
            elem.removeChild(ul_elements[i]);
            return;
        }
    }
}

function addList(element_arr) {
    for (var i = 0; i < element_arr.length; i++) {
        addElement(element_arr[i]);
    }
}

function addDict(element_dict) {
	for (var elem of Object.keys(element_dict)) {
		addElement(element_dict[elem])
	}
}

function selectElement(event) {
	sendInformation(event.target.innerHTML);
}