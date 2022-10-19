from logic.algorithms.weighted_algo import WeightedAlgo
import time

'''
Module containing the class to run the optimized algorithm with a random variable.

Classes: 
    WeightedRandom
'''


class WeightedRandom(WeightedAlgo):
    """
    Class to start the optimized algorithm with a random variable.
    The algorithm should find the best possible seating,
    while the weightings from the pref list get randomly altered.

    ...

    Methods
    --------
    algorithm():
        Overrides super class with given algorithm
    """

    def __init__(self, clas, clas_name, room, room_name):
        super().__init__(clas, clas_name, room, room_name)

    def algorithm(self):
        """
        Updated self.room with created seating!

        :return: void
        """
        print("WeightedRandom not implemented yet!")
        time.sleep(3)
        return []
