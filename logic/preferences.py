import os, time, json, platform

'''
Module to create and read preference lists which can either contain real preferences
or constraints for seating creation.

Functions:
    preferences_create(dictionary, string)
    preferences_edit()
    preferences_delete()
    preferences_read()
    validate_entry(string, int) -> Boolean
    check_int(String) -> Boolean
    clear_screen()
'''

path = os.path.abspath(os.getcwd())
pref_path = path + "/data/preferences/"


def preferences_create(clas, clas_name):
    """
    A function that creates a new empty preference list from a given student list.
    The empty list is then saved as a dictionary in an .json file.
    The user can then edit the list to see fit.

    "Empty" meaning no preferences in this case.

    :param clas: Dictionary of student list
    :param clas_name: Name of student list
    :return: void
    """
    clear_screen()
    pref_dict = {}
    
    try:
        file = open(pref_path + clas_name + ".json", "x")
        file.close()
    except FileExistsError:
        print("Preference list does already exist. Either edit or delete.")
        time.sleep(3)
        return

    # Creation of empty dict to setup
    for studentnr in clas:
        clear_screen()
        new_pref = "0"
        pref_dict[studentnr] = new_pref

    '''
    # Old implementation that goes through every student
    for studentnr in clas:
        clear_screen()
        print("Use the format with the listed studentnumbers or 0's if no preference exists for x1 to x3: x1;x2;x3;y;z.\n x1: 1. Partner\n x2: 2. Partner\n x3: 3. Partner\n y: Should not be Partner (signaled by negative number)\n z: \"front\" or \"back\"\n y and z are optional(e.g. \"1;12;3;-9;front\" or \"3;4;7;back\")")
        for student in clas.items():
            print(student)
        new_pref = input("Please enter the preferences for " + str(clas[studentnr])+ ": ")
        pref_dict[studentnr] = new_pref
    '''

    file = open(pref_path + clas_name + ".json", "w")
    json.dump(pref_dict, file)
    file.close()


def preferences_update(name_class, entry, name):
    """
    Updated the preference list, after being changed by student editing.
    If "r" is entered as a name the entry is removed.

    TODO: implement detection of student occurances in other preferences?

    :param name_class: The name of the student list
    :param entry: The number of the student that changed
    :param name: The name of the student that changed or "r"
    :return: void
    """
    entry = str(entry)
    pref_dict = preferences_read(name_class)
    if name == "r":
        pref_dict.pop(entry)
    else:
        pref_dict[entry] = "0"

    write_file = open(pref_path + name_class + ".json", "w")
    json.dump(pref_dict, write_file)
    write_file.close()
    return


def preferences_edit(student_dict, clas_name):
    """
    Function to edit an existing preference list.

    TODO: catch non-existing

    :return: void
    """
    pref_dict = preferences_read(clas_name)

    while 1:
        print("--- Editing a preference list ---\nEither change the preference or quit with \"done\".")
        for elem in student_dict.keys():
            print(elem + ". " + student_dict[elem] + ": " + str(pref_dict[elem]))

        student = input("Please enter the number of the student which preferences should be changed: ")

        if student.lower() == "done" or student.lower() == "quit" or student.lower() == "q":
            write_file = open(pref_path + clas_name + ".json", "w")
            print("Finished editing.")
            json.dump(pref_dict, write_file)
            write_file.close()
            return

        pref = input("Please enter the new preferences for the student " + student_dict[student] + ": ")
        if not validate_entry(pref, student):
            print("Please enter a valid preference!")
            time.sleep(3)
        else:
            pref_dict[student] = pref


def preferences_delete(name_class):
    """
    Function to delete an existing .json file containing a preference list.

    TODO UPDATE

    :return: void
    """
    if os.path.exists(pref_path + name_class + ".json"):
        os.remove(pref_path + name_class + ".json")
    else:
        print("This list does not exist yet.")
    
    
def preferences_read(name_class):
    """
    Function to read a preference list from an existing .json.

    :param name_class: Name of the connected student list in question
    :return: Dictionary containing the preferences
    """
    pref_dict = {}
    if os.path.exists(pref_path + name_class + ".json"):
        read_file = open(pref_path + name_class + ".json", "r")
        pref_dict = json.load(read_file)
        read_file.close()
    return pref_dict, "SUCCESS"


def validate_entry(entry, studentnr):
    """
    Function to validate the user input for a preference list.
    Valid Inputs are in the form of x;x;x;x;x with a max entry of 5.
    The first four are numerical, and symbolize the other students, the last is empty.

    Should contain...
        ...1-3 positive weightings, no change is a positive weighting indicated by 0.
        ...0-1 negative weighting.
        ...0-1 positional preference, either "front" or "back".

    Neither positive or negative weighting should contain self.

    :param entry: String entry from user
    :param studentnr: Number of student to be validated
    :return: Boolean answering the question
    """

    to_validate = entry.split(";")

    if not to_validate:
        print("List is empty!")
        return False
    elif studentnr in to_validate or "-" + studentnr in to_validate:
        print("Student contained in own preferences!")
        return False
    elif not to_validate[0].isdigit():
        print("No starting Zero!")
        return False
    elif int(to_validate[0]) < 0:
        print("No starting Zero!")
        return False

    pos_pref = 0
    for pref in to_validate:
        if pos_pref == -1:
            if not check_int(pref):
                pos_pref = -2
            elif int(pref) >= 0:
                print("Positive preference after no more allowed!")
                return False
            else:
                pos_pref = -2
        elif pos_pref == -2:
            print("Position statement should be end of preference!")
            return False
        elif not check_int(pref):
            pos_pref = -2
        elif int(pref) <= 0:
            pos_pref = -1
        elif pos_pref > 2:
            print("Positive preference after no more allowed!")
            return False
        else:
            pos_pref = pos_pref + 1

    return True


def check_int(s):
    """
    Simple helper function to check a String to be a Number.

    :param s: String possibly containing a number
    :return: Boolean answering if the String was a number
    """
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


def clear_screen():
    """
    Honestly should be retroactively implemented in a general usage method or smth.
    Clears the console depending on system.

    :return: void
    """
    if platform.system() == "Linux":
        os.system('clear')
    elif platform.system() == "Windows":
        os.system('cls')
    else:
        print("Unsupported System detected. Please either use Windows or Linux.")
        time.sleep(5)
        return


def get_all_pref_lists():
    """
    Simple function to find all preference lists in /data.
    All found lists are then returned as an array.

    :return: Array containing all found lists as String
    """
    file_arr = []

    for file in os.listdir(pref_path):
        if file.endswith(".json"):
            file_arr.append(file[:-5])

    return sorted(file_arr)


def save_preferences(name, pref_str):
    """
    Method to save a dictionary as .json from string.

    :param name: Name of the class
    :param student_str: The students of the class seperated by "|"
    :return: State of the function
    """

    try:
        pref_str = pref_str.split("|")[:-1]
        student_dict = {}
        num = 1

        for pref in pref_str:
            student_dict[num] = pref
            num = num + 1

        file = open(pref_path + name + ".json", "w")
        json.dump(pref_str, file)
        file.close()
        return "SUCCESS"
    except Exception as err:
        print(f"Student saving failed... with Error {err}")
        return "FAIL"