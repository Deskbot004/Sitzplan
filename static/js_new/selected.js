/*
	Is called initially to set various data.

    TODO Not used anymore? Cant seem to bring the console to output

	@return: void
*/
function start(){
    console.log("used start");
    getInformation(data); //depends on own .js
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




//_________________________________Asynchronous Functions_________________________________________________




/*
    Deletes the current file from the server.

	@param confirm: Integer to skip the confirmation
    @return: void
*/
async function deleteInformation(confirm) {
	try {
		var error_case = "Not request fail";
		var rename_request = listRequest();
		rename_request.done(function(data) {
	        console.log("Data has been collected from server!");
	    });
		rename_request.fail(function(xhr, status, error) {
	        error_case = "ERROR " + error.toString();
	    });
		var data_dict = await rename_request;

		var found = 0;
		for (var elem of Object.keys(data_dict)) {
	        if(data_dict[elem] == data) found = 1;
	    }

		if (!found) throw "not_created";

		if (!confirm){
			if (!ask_delete()) throw "canceled";
		}

	    var delete_return = deleteRequest(data);
	    delete_return.done(function(data) {
	        window.location = identity;
	    });
	    delete_return.fail(function(xhr, status, error) {
	        error_case = "ERROR " + error.toString();
	    });
	    await delete_return;
	} catch(err) {
		switch(err) {
			case 'not_created':
				err_text = "The file was never saved!"; break;
			case 'canceled':
				err_text = "Deleting was canceled!"; break;
			default:
				err_text = "Deleting Information went wrong! The file was not deleted!"; break;
		}

		var popup = document.getElementById("popup_del");
		popup.innerHTML = err_text;
		popup.classList.toggle("show");

		switch(typeof err) {
			case "string":
				console.log("Function deleteInformation failed with " + err);break;
			case "object":
				console.log("Delete request failed with "+ error_case);
				console.log(err);
				break;
			default:
				console.log("Undetected Error type: " + typeof err);break;
		}
	}
};


/*
    Sends the string representing the classroom data to the server.

    @return: void
*/
async function saveData(info) {
	try {
		var error_case = "Not request fail";
	    var name = info["name"];

	    if (!checkForIllegalCharacters(name)) throw "illegal";


		/*if (name != data) {
		    rename_value = await renaming(data, name);
			if(!rename_value) throw "exists";
		}*/
	    var data_return = dataToServer(info);

	    data_return.done(function(data) {
	        console.log("Data has been sent to server!");
	    });
	    data_return.fail(function(xhr, status, error) {
	        error_case = "ERROR " + error.toString();
	    });

	    await data_return;
	    //data = name;
	    //throw "saved";
	} catch(err) {
		switch(err) {
			case 'illegal':
				err_text = "Your filename should only contain letters and numbers!"; break;
			case 'exists':
				err_text = "Filename " + name + " already exists!"; break;
			case 'saved':
				err_text = "File saved!"; break;
			default:
				err_text = "Saving file went wrong! The file has not been saved!"; break;
		}

		switch(typeof err) {
			case "string":
				if(err != "saved") console.log("Function sendData failed with " + err);break;
			case "object":
				console.log("Save request failed with "+ error_case);
				console.log(err);
				break;
			default:
				console.log("Undetected Error type: " + typeof err);break;
		}

		var popup = document.getElementById("popup_save");
		popup.innerHTML = err_text;
		popup.classList.toggle("show");
	}
};


/*
	Function that renames a classroom if the name does not already exist.

	@param old_name: Old name of the classroom as String
	@param new_name: New name of the classroom as String
	@return: Boolean if successful or not
*/
async function renaming(old_name, new_name) {
	try {
		var rename_request = listRequest();
		rename_request.fail(function(xhr, status, error) {
	            error_case = "ERROR " + error.toString();
	    });

	    var data_dict = await rename_request;
	    var old_name_exists = 0;

	    for (var elem of Object.keys(data_dict)) {
	        if(data_dict[elem] == new_name) return 0;
	        if(data_dict[elem] == old_name) old_name_exists = 1;
	    }

	    document.getElementById('head_text').innerHTML = document.getElementById('head_text').innerHTML.replace(old_name, new_name);

	    if (old_name_exists) {
	        var delete_return = deleteRequest(old_name);
	        delete_return.done(function(data) {
	            console.log("DELETED RENAMED ROOM");
	        });
	        delete_return.fail(function(xhr, status, error) {
	            error_case = "ERROR " + error.toString();
	        });
	    }

	    return 1;
	} catch (err) {
		alert("Renaming classroom went wrong! An existing old room was not deleted!");
		switch(typeof err) {
			case "string":
				console.log("Function renaming failed with " + err);break;
			case "object":
				console.log("Delete request failed with "+ error_case);
				console.log(err);
				break;
			default:
				console.log("Undetected Error type: " + typeof err);break;
		}
	}
};

