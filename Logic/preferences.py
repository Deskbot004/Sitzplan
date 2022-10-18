import os, time, json, platform

'''
Method to create and read preference lists which can either contain real preferences
or constraints for seating creation.

TODO: finish validate first

TODO: change and finish creation

TODO: nearly all rest functions not done

TODO: see student list linkage

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
    print("--- Create a new preference list ---")
    
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
    return
    
    
def preferences_edit(clas_name):
    """
    Function to edit an existing preference list.

    :return: void
    """
    pref_dict = preferences_read(clas_name)

    return


def preferences_delete(name_class):
    """
    Function to delete an existing .json file containing a preference list.

    :return: void
    """
    clear_screen()
    if os.path.exists(pref_path + name_class + ".json"):
        os.remove(pref_path + name_class + ".json")
    else:
        print("This list does not exist yet. Returning to main menu.")
        time.sleep(3)
        return
    print("Done! Returning to main menu.")
    time.sleep(3)
    return
    
    
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
    return pref_dict


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
