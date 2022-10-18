import os, time, platform
from logic import preferences

'''
Module containing 
'''
path = os.path.abspath(os.getcwd())
seatings_path = path + "/data/seatings/"


class WeightedAlgo:

    def __init__(self, clas, clas_name, room, room_name):
        self.clas = clas
        self.clas_name = clas_name
        self.room = room
        self.room_name = room_name

    def startup(self):
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
