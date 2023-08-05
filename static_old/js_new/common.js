/*
	This js contains all commonly used location swaps.
	Commonly meaning can be accessed from every location.
*/

function switchToClassroom() {
    window.location = "classroom";
}

function switchToHome() {
    window.location = "home";
}

function switchToSeating() {
    window.location = "seating";
}

function switchToStudents() {
    window.location = "student";
}

function switchToAbout() {
    window.location = "about";
}

function switchToPreferences() {
    window.location = "preferences";
}

/*
    Checks whether a text string contains only letters and numbers
    @param str: string to be checked
    @return: Boolean
*/
function checkForIllegalCharacters(str) {
    return /^[A-Za-z0-9 ]*$/.test(str);
}

/*
    Shows the Dropdown Menu, when clicking the three-dots-button
    @param menu_id: id of menu
*/
function showDropdown(menu_id) {
    document.getElementById(menu_id).classList.toggle("hide");
    //Close Dropdown, once you click anything
    document.body.addEventListener("click", function closeDropdown(e) {
        document.getElementById(menu_id).classList.add("hide");
    }, {once : true});
}