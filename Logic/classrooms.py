import os, time, platform

'''
This class handles all interactions with the classrooms.
To access a classroom as a string use the get_classroom(name_room) function.
Rooms are saved as .txt files in data/rooms.

TODO: update create_classroom(), edit_classroom(), delete_classroom()

TODO: replace print_room(room) with a function which shows the room visually in the GUI

TODO: implement room_valid

Functions:
    create_classroom()
    edit_classroom()
    delete_classroom()
    get_classroom(string) -> string
    print_room(string)
    room_valid(room) -> boolean
'''

path = os.path.abspath(os.getcwd())
room_path = path + "/data/rooms/"


def create_classroom():
    """
    This function reads the input of an user to create a list of rows.
    This string is then saved in the subdirectory Data/rooms as a .txt file.
    The user can switch to edit or delete after creation.

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
    print("--- Adding rows ---\n Please enter the rows starting from the back with 0 for empty spots, 1 for avaiable seatings, 2 for seating, which should not be used but shown to be empty later and 3 for the teacher desk (e.g. \"11011\" would be two unconnected tables). Or type \"done\" to finish.")
    while 1:
        new_row = input("Row "+str(row_num)+": ")
        if new_row == "done":
            room = room[:-1]
            break
        room += new_row + ";"
        row_num += 1

    file = open(room_path + name_class + ".txt", "w")
    file.write(room)
    file.close()
    
    while 1:
        action = input("--- Done ---\nPlease check the room you entered. Confirm with \"done\", edit with \"edit\" or delete with \"delete\": ")
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
            print(file.removesuffix(".txt") + "| ", end= ' ')
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
            print(file.removesuffix(".txt") + "| ", end= ' ')
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


def get_classroom(name_room):
    """
    This function returns a room from an existing .txt file.

    :param name_room: Name of the room as a string
    :return: String containing the room information
    """

    room = ""
    if os.path.exists(room_path + name_room + ".txt"):
        read_file = open(room_path + name_room + ".txt", "r")
        room = read_file.read()
        read_file.close()
    return room


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


def room_valid(room):
    """
    Check function to see if the room, that was created is valid.
    Valid meaning, at least one empty seat for a student.
    At least one teacher desk.

    :param room: Name of the room as a string
    :return: Boolean that answers the question
    """
    print("not implemented yet")
    time.sleep(3)
    return
