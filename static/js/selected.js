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
    Deletes the current classroom from the server.

    @return: void
*/
function deleteInformation() {
    var test = $.post("/delclassroom", { "result": data }, function(data) {alert("Classroom deleted");switchToClassroom();});
};

/*
    Fill grid with information if a classroom is loaded from the server.

    @param text: string of the classroom name
    @return: void
*/
function getInformation(text){
    var info = $.post("/getclassroomlists", {"result": text}, function(data) {fillGrid(classroom, grid, data);});
};
