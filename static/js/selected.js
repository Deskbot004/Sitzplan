/*
	Is called initially to set various data.

	@return: void
*/
function start(){
    getInformation(data);
    document.getElementById('head_text').innerHTML = document.getElementById('head_text').innerHTML.replace("free", data);
    document.getElementById('filename').value = data;
};

/*
	Asks the user if he really wants to delete the data which was selected.

	@return: Boolean if the user wants to delete
*/
function ask_delete() {
	var ask_text = "Are you sure that you want to delete free?";
	ask_text = ask_text.replace("free", data);
	return confirm(ask_text);
}