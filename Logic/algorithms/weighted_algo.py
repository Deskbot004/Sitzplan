import os, time, platform
from logic import preferences
from datetime import date
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

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
    room : string
        The room information
    room_name : string
        The room name
    seatings_path : string
        The path to the seating data
    result : array
        At first an empty array before the result gets saved

    Methods
    -----------
    startup():
        Exists to interact with preference lists.
    algorithm():
        Exists as a stub for subclasses to use.
    save_result():
        Saves the created result in image (.png) and text (.txt) form
    create_image():
        Creates an image from the result and saves the plt as .pkl
    show_result():
        Displays the image
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
        self.result = []

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
                self.result = self.algorithm()
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
        return ""

    def save_result(self):
        """
        Function to save the result as an image and as text.

        TODO: Update to fit into class, as it was copied

        :return: void
        """
        try:
            file = open(self.seatings_path + self.clas_name + self.room_name + ".txt", "x")
        except FileExistsError:
            file = open(self.seatings_path + self.clas_name + self.room_name + ".txt", "w")

        with open(self.seatings_path + self.clas_name + self.room_name + ".txt", 'w') as fid:
            ax = pickle.load(fid)

        plt.savefig(self.seatings_path + self.clas_name + "_" + self.room_name + "_" + str(date.today()) + ".png",
                    dpi=300)

        print("Image saved in " + self.seatings_path + ". Returning to main menu.")

        room_list = ""
        for element in self.room:
            for name in element:
                room_list += name + ","
            room_list = room_list[:-1]
            room_list += ";"
        room_list = room_list[:-1]

        file.write(room_list)
        file.close()
        time.sleep(5)
        return

    def create_image(self):
        """
        Function to create an image from the result and saves the plt for later usage.

        TODO: update room mentions to result where it is fit

        :return: void
        """

        fig, ax = plt.subplots()

        fig.patch.set_visible(False)
        ax.axis('off')
        ax.axis('tight')

        # expects each room to be at least 2 spaces wide
        info_arr = ["" for x in range(len(self.room[0]))]
        info_arr[0] = "Class: " + self.clas_name
        info_arr[len(self.room[0]) - 1] = "Room: " + self.room_name

        df = pd.DataFrame(np.array(self.room), columns=info_arr)

        ax.table(cellText=df.values, colLabels=df.columns, loc='center')
        fig.tight_layout()

        with open(self.seatings_path + self.clas_name + self.room_name + ".txt", 'w') as fid:
            pickle.dump(ax, fid)

    def show_result(self):
        """
        Simple function to show the result of a finished algorithm as an image

        :return: void
        """
        with open(self.seatings_path + self.clas_name + self.room_name + ".txt", 'w') as fid:
            ax = pickle.load(fid)
        plt.show()  # pip install pyqt5