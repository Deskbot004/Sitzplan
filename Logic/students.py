import time, os, json, platform
from logic import preferences

'''
This Module handles all interaction with students and their respective lists.
To access a student list as a dictionary call the get_student_list(name_class) function.
Student lists are saved as .json files in data/classes.

TODO: update save_students(), edit_students(), delete_students()

Functions:
    save_students()
    edit_students()
    delete_students()
    get_student_list(string) -> dictionary
    get_all_student_list() -> array
'''

path = os.path.abspath(os.getcwd())
class_path = path + "/data/classes/"


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


def get_student_list(name_class):
    """
    This function reads a student list as a dictionary from a .json file and returns it.

    :param name_class: Name of the student list which should be accessed as String
    :return: Dictionary of the student list
    """

    student_dict = {}
    if os.path.exists(class_path + name_class + ".json"):
        read_file = open(class_path + name_class + ".json", "r")
        student_dict = json.load(read_file)
        read_file.close()
    return student_dict


def get_all_student_lists():
    """
    Simple function to find all student lists in /data.
    All found lists are then returned as an array.

    :return: Array containing all found lists as String
    """
    file_arr = []

    for file in os.listdir(class_path):
        if file.endswith(".json"):
            file_arr.append(file[:-5])

    return file_arr
