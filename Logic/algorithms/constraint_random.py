from logic.algorithms.weighted_algo import WeightedAlgo
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

    def __init__(self, clas, clas_name, room, room_name):
        super().__init__(clas, clas_name, room, room_name)

    def algorithm(self):
        """

        :return:
        """
        print("ConstraintRandom not implemented yet!")
        time.sleep(3)
        return
