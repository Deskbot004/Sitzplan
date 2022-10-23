/*
	Is called initially to set various data.

	@return: void
*/
function start(){
    getInformation(data);
    document.getElementById('head_text').innerHTML = document.getElementById('head_text').innerHTML.replace("free", data);
    document.getElementById('filename').value = data;
};