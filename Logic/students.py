import  os, json

'''
This Module handles all interaction with students and their respective lists.
To access a student list as a dictionary call the get_student_list(name_class) function.
Student lists are saved as .json files in data/classes.

Functions:
    get_student_list(string) -> dictionary, state
    get_all_student_list() -> array, state
    save_students(string, string) -> state
    delete_students(string) -> state
'''

path = os.path.abspath(os.getcwd())
class_path = path + "/data/classes/"


def get_student_list(name_class):
    """
    This function reads a student list as a dictionary from a .json file and returns it.

    :param name_class: Name of the student list which should be accessed as String
    :return: Dictionary of the student list, State of the function
    """

    try:
        read_file = open(class_path + name_class + ".json", "r")
        student_dict = json.load(read_file)
        read_file.close()
        return student_dict, "SUCCESS"
    except Exception as err:
        print(f"Student getting failed... with Error {err}")
        return {}, "FAIL"


def get_all_student_lists():
    """
    Simple function to find all student lists in /data.
    All found lists are then returned as an array.

    :return: Array containing all found lists, State of the function
    """

    try:
        file_dict = {}
        entry = 1

        for file in os.listdir(class_path):
            if file.endswith(".json"):
                file_dict[entry] = file[:-5]
                entry = entry + 1

        # Sort by value
        file_dict = {int(k): v for k, v in file_dict.items()}
        file_dict = dict(sorted(file_dict.items()))
        file_dict = {str(k): v for k, v in file_dict.items()}

        return file_dict, "SUCCESS"
    except Exception as err:
        print(f"Student list getting failed... with Error {err}")
        return {}, "FAIL"


def save_students(name, student_str):
    """
    Method to save a dictionary as .json from string.

    :param name: Name of the class
    :param student_str: The students of the class seperated by "|"
    :return: State of the function
    """

    try:
        student_str = student_str.split("|")[:-1]
        student_dict = {}
        num = 1

        for student in student_str:
            student_dict[num] = student
            num = num + 1

        file = open(class_path + name + ".json", "w")
        json.dump(student_str, file)
        file.close()
        return "SUCCESS"
    except Exception as err:
        print(f"Student saving failed... with Error {err}")
        return "FAIL"


def delete_students(name):
    """
    Method to delete a .json file containing a class.

    :param name: String containing the name of the class to be deleted
    :return: State of the function
    """

    try:
        os.remove(class_path + name + ".json")
        return "SUCCESS"
    except Exception as err:
        print(f"Student deleting failed... with Error {err}")
        return "FAIL"


'''
def save_students():
    """
    This function reads the input of an user to create a dictionary with "number:name" pairs of students.
    The numbers do not indicate any sorting but are simply chosen to be unique for each student.
    This dictionary is then saved in the subdirectory data/classes as a .json file.
    The user can switch to edit or delete after creation.
    For the best visualisation use the same number of letters for everyone.

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
    
    name_class = input("--- Save a new student list --- \nPlease enter the name of the class e.g. \"5a\": ")

    if name_class.lower() == "quit" or name_class.lower() == "q":
        return

    try:
        file = open(class_path + name_class + ".json", "x")
        file.close()
    except FileExistsError:
        print("If you want to modify the class chose the edit option.")
        time.sleep(3)
        return
    
    students = 1
    student_dict = {}
    print("--- Adding students ---\n Finish by typing \"done\"")
    while 1:
        new_name = input("Please enter the name of the " + str(students) + ". student: ")
        if new_name == "done":
            break
        student_dict[students] = new_name
        students += 1

    for student in student_dict.items():
        print(student)
    
    file = open(class_path + name_class + ".json", "w")
    json.dump(student_dict, file)
    file.close()

    while 1:
        action = input("--- Done ---\nPlease check the list you entered. Confirm with \"done\", edit with \"edit\" or delete with \"delete\": ")
        if action.lower() == "done":
            print("File saved. Returning to main menu.")
            preferences.preferences_create(student_dict, name_class)
            time.sleep(3)
            return
        elif action.lower() == "edit":
            edit_students()
            return
        elif action.lower() == "delete":
            delete_students()
            return
        else:
            print("Please choose a given option.")
        

def edit_students():
    """
    This function allows the user to edit an existing class read from a .json file.
    Adding a student creates a new entry with the lowest possible free number in the dictionary.
    Deleting a student simply removes an entry and does not shift numbers to fit.

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
    
    print("--- Edit a student list ---\n!Please remember to update the preference list later!\nExisting classes:")
    
    for file in os.listdir(class_path):
        if file.endswith(".json"):
            print(file[:-5]+ " |")
    print("")
        
    name_class = input("Please enter the name of the class: ")
    
    if name_class.lower() == "quit" or name_class.lower() == "q":
        return

    update_dict = {}
    student_dict = get_student_list(name_class)
    while 1:
        print("Current class members:")

        # Sort by value
        student_dict = {int(k): v for k, v in student_dict.items()}
        student_dict = dict(sorted(student_dict.items()))
        student_dict = {str(k): v for k, v in student_dict.items()}

        for student in student_dict.items():
            print(student)
        action = input("Choose your action:\n 1: Add a new student\n 2: Delete a student\n 3: Change the name of a student\n 4: Search if a student is in the list\n 5: Finish editing\nChosen action: ")
        if action.lower() == "quit" or action.lower() == "q":
            return
    
        if action == "1":
            dict_length = len(student_dict)
            new_name = input("Please enter the name of the new student: ")
            
            for number in range(dict_length):
                if student_dict.get(str(number + 1)) == None:
                    student_dict[str(number + 1)] = new_name
                    update_dict[str(number + 1)] = new_name
                    break
                elif number + 1 == dict_length:
                    student_dict[str(number + 2)] = new_name
                    update_dict[str(number + 2)] = new_name
        elif action == "2":
            to_remove = input("Please enter the number of the student to be removed: ")
            student_dict.pop(to_remove)
            update_dict[to_remove] = "r"
        elif action == "3":
            to_edit = input("Please enter the number of the student to be edited: ")
            new_name = input("Please enter the new name of the student: ")
            student_dict.update({to_edit: new_name})
        elif action == "4":
            search_name = input("Please enter the name to search: ")
            if search_name in student_dict.values():
                print("The student is in the dictionary.")
                time.sleep(3)
            else:
                print("The student is NOT in the dictionary.")
                time.sleep(3)
        elif action == "5":
            write_file = open(class_path + name_class + ".json", "w")
            print("Finished editing. Returning to main menu.")
            json.dump(student_dict, write_file)
            write_file.close()
            for number in update_dict:
                preferences.preferences_update(name_class, number, update_dict[number])
            return
        else:
            print("Please enter an existing command.")


def delete_students():
    """
    This function deletes an existing .json file containing a student list.

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
    
    print("--- Delete a student list ---\nExisting classes:")
    
    for file in os.listdir(class_path):
        if file.endswith(".json"):
            print(file[:-5]+ " |")
    print("")
        
    name_class = input("Please enter the name of the class: ")
    
    if name_class.lower() == "quit" or name_class.lower() == "q":
        return
    
    if os.path.exists(class_path + name_class + ".json"):
        os.remove(class_path + name_class + ".json")
    else:
        print("This class does not exist yet. Returning to main menu.")
        time.sleep(3)
        return
    print("Done! Returning to main menu.")
    time.sleep(3)
    return
'''

