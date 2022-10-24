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

	@return: void
*/
function ask_delete() {
	var ask_text = "Are you sure that you want to delete free?";
	ask_text = ask_text.replace("free", data);
	if(confirm(ask_text)) {
		deleteInformation();
	}
}