from logic import students, classrooms


class File:
    """
        Class that saves every important aspect of a file.

        :param name: File name as found in data
        :param data: Content of the file
        :param access: Either a 0 if no user is using this file at the moment or 1
    """
    def __init__(self, name, data, access):
        self.name = name
        self.data = data
        self.access = access


def ini_dict(in_data_dict):
    """
        Function that reads all existing files in data and creates a multi-structure to edit.
        First layer: Dictionary with keys depicting the type of data
        Second layer: Arrays containing the different files of that type
        Third layer: File Objects which contain every important information of the file

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
    in_data_dict["classrooms"] = room_arr

    # Interpret all student lists
    studentlists = students.get_all_student_lists()[0]
    studentlist_arr = []
    for student_key in studentlists:
        student_name = studentlists[student_key]
        student_data = students.get_student_list(student_name)[0]
        studentlist_arr.append(File(student_name, student_data, 0))
    in_data_dict["studentlists"] = studentlist_arr
    return in_data_dict


def save_dict(in_data_dict):
    """
    Saves the dict into different files.

    TODO add try except
    """
    call = "FAIL"
    for file_type in in_data_dict:
        to_save = in_data_dict[file_type]
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


def list_filetype(data_dict, filetype):
    """
        Method to list all available files of a given filetype as a dictionary.

        :param data_dict: Array containing the cache data
        :param filetype: The type of the filetype that should be listed
        :return: The created dictionary and the state of the function
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
        :return:
    """
    for file_obj in data_dict[filetype]:
        if file_obj.name == name:
            return file_obj.data, "SUCCESS"
    return {}, "FAIL"
