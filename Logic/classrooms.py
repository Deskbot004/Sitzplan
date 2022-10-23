import os

'''
This Module handles all interactions with the classrooms.
To access a classroom as a string use the get_classroom(name_room) function.
Rooms are saved as .txt files in data/rooms.


Functions:
    save_classroom(string, string, string)
    get_classroom(string) -> string
    get_classroom_untrimmed(string) -> string
    get_all_classroom_lists() -> array
    delete_classroom_web(string)
'''

path = os.path.abspath(os.getcwd())
room_path = path + "/data/rooms/"


def save_classroom(class_name, class_information, class_information_trimmed):
    """
    A function to save the information of a classroom in /data.

    :param class_name: Name of the room to be saved
    :param class_information: Information about the classroom untrimmed for the editor
    :param class_information_trimmed: Information about the classroom trimmed for the algorithm
    :return: void
    """

    file = open(room_path + class_name + ".txt", "w")
    file.write(class_information_trimmed)
    file.close()

    file = open(room_path + class_name, "w")
    file.write(class_information)
    file.close()


# needed for algorithm later
def get_classroom(name_room):
    """
    This function returns a trimmed room from an existing .txt file.

    :param name_room: Name of the room as a string
    :return: String containing the room information
    """

    room = ""
    if os.path.exists(room_path + name_room + ".txt"):
        read_file = open(room_path + name_room + ".txt", "r")
        room = read_file.read()
        read_file.close()
    return room


def get_classroom_untrimmed(name_room):
    """
    This function returns a untrimmed room from an existing file.

    :param name_room: Name of the room as a string
    :return: String containing the room information
    """

    room = ""
    if os.path.exists(room_path + name_room):
        read_file = open(room_path + name_room, "r")
        room = read_file.read()
        read_file.close()
    return room


def get_all_classroom_lists():
    """
    Simple function to find all classroom lists in /data.
    All found lists are then returned as an array.

    :return: Array containing all found lists as String
    """
    file_dict = {}
    entry = 1

    for file in os.listdir(room_path):
        if file.endswith(".txt"):
            file_dict[entry] = file[:-4]
            entry = entry + 1

    # Sort by value
    file_dict = {int(k): v for k, v in file_dict.items()}
    file_dict = dict(sorted(file_dict.items()))
    file_dict = {str(k): v for k, v in file_dict.items()}

    return file_dict


def delete_classroom_web(name):
    """
    Deletes an existing classroom from webpage.

    :param name: Name of the room to be deleted
    :return: void
    """
    os.remove(room_path + name + ".txt")


'''
not relevant for web implementation anymore
def create_classroom():
    """
    This function reads the input of an user to create a list of rows.
    This string is then saved in the subdirectory Data/rooms as a .txt file.
    The user can switch to edit or delete after creation.

    The saved numbers have the following meaning:
        0 = No seating here, for example ground
        1 = Seating available
        2 = Seating available but should be left empty
        3 = Teacher desk

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

    name_class = input("--- Create a new classroom --- \nPlease enter the name of the classroom e.g. \"A001\": ")

    try:
        file = open(room_path + name_class + ".txt", "x")
        file.close()
    except FileExistsError:
        print("If you want to modify the class chose the edit option.")
        time.sleep(3)
        return

    if name_class.lower() == "quit" or name_class.lower() == "q":
        return

    room = ""
    row_num = 0
    print(
        "--- Adding rows ---\n Please enter the rows starting from the back with 0 for empty spots, 1 for avaiable seatings, 2 for seating, which should not be used but shown to be empty later and 3 for the teacher desk (e.g. \"11011\" would be two unconnected tables). Or type \"done\" to finish.")
    while 1:
        new_row = input("Row " + str(row_num) + ": ")
        if new_row == "done":
            room = room[:-1]
            break
        room += new_row + ";"
        row_num += 1

    file = open(room_path + name_class + ".txt", "w")
    file.write(room)
    file.close()

    while 1:
        action = input(
            "--- Done ---\nPlease check the room you entered. Confirm with \"done\", edit with \"edit\" or delete with \"delete\": ")
        if action.lower() == "done":
            print("File saved. Returning to main menu.")
            time.sleep(3)
            return
        elif action.lower() == "edit":
            edit_classroom()
            return
        elif action.lower() == "delete":
            delete_classroom()
            return
        else:
            print("Please choose a given option.")


def edit_classroom():
    """
    This function allows the editing of existing rows in an existing classroom.
    The option to add or shift rows is not implemented.

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

    print("--- Edit a classroom ---\nExisting rooms:")

    for file in os.listdir(room_path):
        if file.endswith(".txt"):
            print(file[:-4] + " |")
    print("")

    name_room = input("Please enter the name of the room e.g. \"A001\": ")

    if name_room.lower() == "quit" or name_room.lower() == "q":
        return

    room = get_classroom(name_room)
    room = room.split(";")
    print_room(room)
    while 1:
        row_num = input("Please enter the row you would like to change or \"done\": ")
        if row_num.lower() == "quit" or row_num.lower() == "q" or row_num == "done":
            write_file = open(room_path + name_room + ".txt", "w")
            room_new = ""
            for row in room:
                room_new += row + ";"
            room_new = room_new[:-1]
            write_file.write(room_new)
            write_file.close()
            return
        new_row = input("Please enter the new row: ")

        room[int(row_num)] = new_row
        print_room(room)


def delete_classroom():
    """
    This function deletes an existing .txt file containing a room.

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
    
    print("--- Delete a classroom ---\nExisting rooms:")
    
    for file in os.listdir(room_path):
        if file.endswith(".txt"):
            print(file[:-4]+ " |")
    print("")
        
    name_room = input("Please enter the name of the room e.g. \"A001\": ")
    
    if name_room.lower() == "quit" or name_room.lower() == "q":
        return
    
    if os.path.exists(room_path + name_room + ".txt"):
        os.remove(room_path + name_room + ".txt")
    else:
        print("This room does not exist yet. Returning to main menu.")
        time.sleep(3)
        return
    print("Done! Returning to main menu.")
    time.sleep(3)
    return

def print_room(room):
    """
    This function is a helper function to easily print a room.
    Should be majorly updated soon.

    :param room: Name of the room as a string
    :return: void
    """

    rows = 0
    for x in room:
        print("Row "+str(rows)+": "+x)
        rows += 1
'''