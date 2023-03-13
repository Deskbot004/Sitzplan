/*
	This js contains all requests that can be generalised.


	Request functions:
		dataToServer(dictionary) -> request
		listRequest() -> request
		requestInformation(string) -> request
*/




/*
    Requests data to be saved on the server.
    Location depends on identity.

    @param name: Data to be saved
    @return: Request
*/
function dataToServer(send_data) {
    return $.post("/"+ identity +"_info", send_data);
};


/*
	Requests the list of every file relating to identity.

	@return: Request
*/
function listRequest() {
    return $.get("/get"+ identity +"lists");
};


/*
    Requests the content of a file from the server.
    Which file is requested depends on identity and the given string.

    @param text: String of the file name
    @return: Request
*/
function requestInformation(data_name){
    return $.post("/get"+ identity +"lists", {"result": data_name});
};


/*
    Requests the deletion of a specified file from the Server.
    Which file is requested depends on identity and the given string.

    @param del_name: String of the file name
    @return: Request
*/
function deleteRequest(del_name) {
	return $.post("/del"+ identity, { "result": del_name });
};