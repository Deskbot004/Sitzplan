from logic.algorithms.weighted_algo import WeightedAlgo
from logic import preferences as pref
import time


'''
Module containing the class to run the random algorithm with constraints.
    
Classes: 
    ConstraintRandom
'''


class ConstraintRandom(WeightedAlgo):
    """
    Class to start the random algorithm with constraints.
    Main focus here lies on only focusing on the constraints given from the pref list,
    while still creating a otherwise completely random seating.

    ...

    Methods
    --------
    algorithm():
        Overrides super class with given algorithm
    """

    def __init__(self, clas, clas_name, room, room_name, pref_name):
        super().__init__(clas, clas_name, room, room_name, pref_name)

    def algorithm(self):
        """
        Update room with created seating

        :return: Updated room
        """
        try:
            room = self.room[0].split(";")
            pref_list = pref.preferences_read(self.pref_name)

            return room

        except Exception as err:
            print("Caught this error: " + repr(err))
            return "FAIL"


