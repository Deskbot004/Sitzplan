from logic import students, classrooms

'''
Module to handle all cache interactions.
Additionally this module should be the only interface between the cache and the files.

Classes:
    File(self, string, dictionary, int)
    
Functions:
    ini_dict(dictionary) -> dictionary, state
    save_dict(dictionary) -> state
    clean_folder(dictionary) -> state
    list_filetype(dictionary, string) -> dictionary
    get_file_data(dictionary, string, string) -> var
    delete_file_data(dictionary, string, string) -> dictionary
    delete_file_data(dictionary, string, string, var) -> dictionary
    rename_file_data(dictionary, string, string, string) -> dictionary
'''


class File:
    """
    Class that saves every important aspect of a file.

    :param name: File name as found in data
    :param data: Content of the file
    :param access: Different meanings:
                    0: not accessed
                    1: accessed by a user
    """
    def __init__(self, name, data, access):
        self.name = name
        self.data = data
        self.access = access


def ini_dict(data_dict):
    """
    Function that reads all existing files in data and creates a multi-structure to edit.
    First layer: Dictionary with keys depicting the type of data
    Second layer: Arrays containing the different files of that type
    Third layer: File Objects which contain every important information of the file

    :param data_dict: Empty cache given from the server
    :return: Initialized cache, state of the function
    TODO add try except
    """
    # Interpret all room files
    # Example call:
    # data_dict["rooms"][0].name => Name of the first found room
    rooms = classrooms.get_all_classroom_lists()[0]
    room_arr = []
    for room_key in rooms:
        room_name = rooms[room_key]
        room_data = classrooms.get_classroom(room_name)[0]
        room_arr.append(File(room_name, room_data, 0))
    data_dict["classrooms"] = room_arr

    # Interpret all student lists
    studentlists = students.get_all_student_lists()[0]
    studentlist_arr = []
    for student_key in studentlists:
        student_name = studentlists[student_key]
        student_data = students.get_student_list(student_name)[0]
        studentlist_arr.append(File(student_name, student_data, 0))
    data_dict["studentlists"] = studentlist_arr
    return data_dict


def save_dict(data_dict):
    """
    Saves the cache into different files.

    :param data_dict: Cache to be converted into files
    :return: state of the function
    TODO add try except
    """
    call = "FAIL"
    for file_type in data_dict:
        to_save = data_dict[file_type]
        if file_type == "classrooms":
            for file_obj in to_save:
                call = classrooms.save_classroom(file_obj.name, file_obj.data)
        elif file_type == "studentlists":
            for file_obj in to_save:
                call = students.save_students(file_obj.name, file_obj.data)
        else:
            print("Warning: unknown file_type saved:")
            print(file_type)
            call = "FAIL"
    return call


# redundant
def clean_folder(data_dict):
    """
    Deletes every file which was deleted in runtime.

    :param data_dict: Cache from the server
    :return: State of the function
    TODO ADD TRY CATCH
    """
    call = "NONE DELETED"
    rooms = classrooms.get_all_classroom_lists()[0]
    data_rooms = list_filetype(data_dict, "classrooms")[0]
    studentlists = students.get_all_student_lists()[0]
    data_studentlists = list_filetype(data_dict, "studentlists")[0]
    for room in rooms.values():
        if room not in data_rooms.values():
            call = classrooms.delete_classroom(room)
    for studentlist in studentlists.values():
        if studentlist not in data_studentlists.values():
            call = students.delete_students(studentlist)
    return call


def list_filetype(data_dict, filetype):
    """
    Method to list all available files of a given filetype as a dictionary.

    :param data_dict: Array containing the cache data
    :param filetype: The type of the filetype that should be listed
    :return: The created dictionary and the state of the function
    TODO REMOVE STATE /TRY CATCH
    """
    try:
        list_dict = {}
        counter = 0
        for file_obj in data_dict[filetype]:
            counter += 1
            list_dict[counter] = file_obj.name
        return list_dict, "SUCCESS"
    except Exception as err:
        print(f"Listing available files failed with Error {err}")
        return {}, "FAIL"


def get_file_data(data_dict, filetype, name):
    """
    Get the data from a file, and lock the access!

    :param data_dict: Array containing the cache data
    :param filetype: The type of the filetype that should be listed
    :param name: The name of the file to get
    :return: Information contained in the file
    TODO ACCESS LOCK AND CATCHING / Remove state
    """
    for file_obj in data_dict[filetype]:
        if file_obj.name == name:
            return file_obj.data, "SUCCESS"
    return {}, "FAIL"


def delete_file_data(data_dict, filetype, name):
    """
    Remove a file from the cache

    :param data_dict: Cache from the server
    :param filetype: Filetype to be deleted
    :param name: Name of the file to be deleted
    :return: Updated cache
    TODO REMOVE STATE
    """
    for file_obj in data_dict[filetype]:
        if file_obj.name == name:
            data_dict[filetype].remove(file_obj)
    return data_dict, "SUCCESS"


def save_file_data(data_dict, filetype, name, data):
    """
   Add a file to the cache

   :param data_dict: Cache from the server
   :param filetype: Filetype to be saved
   :param name: Name of the file to be saved
   :param data: Information to be saved
   :return: Updated cache
   TODO REMOVE STATE
    """
    if filetype == "studentlists":
        data = students.string_converter(data)
    data_dict[filetype].append(File(name, data, 0))
    return data_dict, "SUCCESS"


# On that note how the fuck wird gerade das renaming verwaltet???
def rename_file_data(data_dict, filetype, name, new_name):
    """
    Try to rename a file with the new name given.
    Return FAIL if no such file exists.

    :param data_dict: Cache from the server
    :param filetype: Filetype to be renamed
    :param name: Name of the file to be renamed
    :param new_name: New name for the file
    :return: Updated cache, state
    TODO update in other functions, does not check if new name already exists
    """
    data = ""
    for file_obj in data_dict[filetype]:
        if file_obj.name == name:
            data = file_obj.data
            data_dict = delete_file_data(data_dict, filetype, name)
            data_dict = save_file_data(data_dict, filetype, new_name, data)
            return data_dict, "SUCCESS"
    return {}, "FAIL"



