from logic.algorithms.weighted_algo import WeightedAlgo
from logic import preferences as pref
import time
import math


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

    def __init__(self, clas, clas_name, room, room_name, pref):
        super().__init__(clas, clas_name, room, room_name, pref)

    def algorithm(self):
        """
        Update room with created seating

        :return: Updated room
        """

        format_room = self.room.split(";")[:-1]
        seating_order = format_room.reverse()   # reversed because the last element is the first row!
        seatable_rows = [i for i, row in zip(range(len(format_room)), format_room) if "1" in row]
        front_end_seatable = math.ceil(len(seatable_rows) * 0.3) - 1
        front_end_total = seatable_rows[math.ceil(len(seatable_rows) * 0.3)] - 1
        front_preferred_students = [student for student in self.pref.keys() if self.pref[student][4] != "empty"]
        print(front_preferred_students)
        # fill seats
        for row in seating_order:
            for seat in row:



        return format_room



