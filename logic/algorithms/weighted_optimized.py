from logic.algorithms.weighted_algo import WeightedAlgo
import time

'''
Module containing the class to run the optimized algorithm.

Classes: 
    WeightedOptimized
'''


class WeightedOptimized(WeightedAlgo):
    """
    Class to start the optimized algorithm.
    The algorithm is focused on finding the best possible seating.

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
        Update self.room with created seating!

        :return: void
        """
        FIRST_PREF_VAL = 10
        SECOND_PREF_VAL = 6
        THIRD_PREF_VAL = 2
        DOUBLE_PREF_MULT = 3
        return
