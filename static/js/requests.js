/*
	This js contains all requests that can be generalised.


	Request functions:
		dataToServer(dictionary) -> request
		listRequest()
*/




/*
    Requests a classroom to be saved on the server.

    @param name: Name of the classroom
    @param layout_array: Array containing the room information
    @return: Request
*/
function dataToServer(send_data) {
    return $.post("/"+ identity +"_info", send_data);
};


/*
	Requests the list of all classrooms.

	@param text: List of the classrooms
	@return: Request
*/
function listRequest() {
    return $.get("/get"+ identity +"lists");
};


/*
    Requests the classroom information from server.

    @param text: String of the classroom name
    @return: Request
*/
function requestInformation(data_name){
    return $.post("/get"+ identity +"lists", {"result": data_name});
};


/*
    Requests the deletion of the specified classroom.

    @param del_name: Classroom to be deleted
    @return: Request
*/
function deleteRequest(del_name) {
	return $.post("/del"+ identity, { "result": del_name });
};