import os, time, platform
from logic import preferences

'''
Module containing the super class for all weighted algorithms.

TODO: Create generic functions for all algorithms e.g. Saving/showing the image

Classes:
    WeightedAlgo
'''


class WeightedAlgo:
    """
    Class for every weighted algorithm.

    ...

    Attributes
    -----------
    clas : dictionary
        Contains the student list
    clas_name : string
        The name of the student list
    room: string
        The room information
    room_name: string
        The room name
    seatings_path: string
        The path to the seating data

    Methods
    -----------
    startup():
        Exists to interact with preference lists.
    algorithm():
        Exists as a stub for subclasses to use.
    """
    def __init__(self, clas, clas_name, room, room_name):
        """
        Constructs all attributes necessary for the algorithm

        :param clas: Contains the student list
        :param clas_name: The name of the student list
        :param room: The room information
        :param room_name: The room name
        """
        self.clas = clas
        self.clas_name = clas_name
        self.room = room
        self.room_name = room_name
        path = os.path.abspath(os.getcwd())
        self.seatings_path = path + "/data/seatings/"

    def startup(self):
        """
        Starts the preference list selection and editing process, until the algorithm is started.

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

        while 1:
            print(" --- Weighted algorithm ---\nPlease choose an option.\n 1: Use an existing preference list\n 2: Create a new one\n 3: Edit an existing one\n 4: Delete a preference list\n 5: Return")
            action = input("Chosen option: ")
            if action == "1":
                self.algorithm()
            elif action == "2":
                preferences.preferences_create(self.clas, self.clas_name)
            elif action == "3":
                preferences.preferences_edit(self.clas, self.clas_name)
            elif action == "4":
                preferences.preferences_delete(self.clas_name)
            elif action.lower() == "quit" or action.lower() == "q" or action == "5":
                return
            else:
                print("Please choose an existing option.")
                time.sleep(3)

    def algorithm(self):
        print("Only stub for real implementations in sub classes!")
        return
