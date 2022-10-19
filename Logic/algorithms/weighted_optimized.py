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

    def __init__(self, clas, clas_name, room, room_name):
        super().__init__(clas, clas_name, room, room_name)

    def algorithm(self):
        """
        Updated self.room with created seating!

        :return: void
        """
        print("WeightedOptimized not implemented yet!")
        time.sleep(3)
        return
