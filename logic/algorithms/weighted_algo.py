import os
from PIL import Image
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
        The room information which gets updated by the algorithm
    room_name : string
        The room name
    seatings_path : string
        The path to the seating data

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

    def __init__(self, clas, clas_name, room, room_name, pref):
        """
        Constructs all attributes necessary for the algorithm

        :param clas: Contains the student list
        :param clas_name: The name of the student list
        :param room: The room information
        :param room_name: The room name
        :param pref: The preference list of the class
        """
        self.clas = clas
        self.clas_name = clas_name
        self.room = room
        self.room_name = room_name
        self.pref = pref
        path = os.path.abspath(os.getcwd())
        self.seatings_path = path + "/data/seatings/"
        self.pref_path = path + "/data/preferences/"
        self.image_path = path + "/static/seatings/"

    def startup(self):
        """
        Starts the preference list selection and editing process, until the algorithm is started.

        :return: -1 for error case so that the programm does not try to create an image
        """
        self.algorithm()

    def algorithm(self):
        print("Only stub for real implementations in sub classes!")
        return

    def save_result(self):
        """
        Function to save the result as an image and as text.

        :return: Name of the image
        """

        try:
            file = open(self.seatings_path + self.clas_name + self.room_name + str(date.today()) + ".txt", "x")
        except FileExistsError:
            file = open(self.seatings_path + self.clas_name + self.room_name + str(date.today()) + ".txt", "w")

        with open(self.seatings_path + self.clas_name + self.room_name + ".pkl", 'rb') as fid:
            ax = pickle.load(fid)

        filename = self.clas_name + "_" + self.room_name + "_" + str(date.today()) + ".png"
        plt.savefig(self.image_path + filename, dpi=300)

        im = Image.open(self.image_path + filename)
        im = im.crop(im.getbbox())
        im.save(self.image_path + filename)

        print("Image saved in " + self.seatings_path + ".")

        room_list = ""
        for element in self.room:
            for name in element:
                room_list += name + ","
            room_list = room_list[:-1]
            room_list += ";"
        room_list = room_list[:-1]

        file.write(room_list)
        file.close()
        plt.close()
        return filename

    def create_image(self):
        """
        Function to create an image from the result and saves the plt for later usage.

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

        with open(self.seatings_path + self.clas_name + self.room_name + ".pkl", 'wb') as fid:
            pickle.dump(ax, fid)
        plt.close()

    def show_result(self):
        """
        Simple function to show the result of a finished algorithm as an image.

        :return: void
        """
        with open(self.seatings_path + self.clas_name + self.room_name + ".pkl", 'rb') as fid:
           ax = pickle.load(fid)
        plt.show()
