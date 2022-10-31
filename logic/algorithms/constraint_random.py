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

    def __init__(self, clas, clas_name, room, room_name, pref):
        super().__init__(clas, clas_name, room, room_name, pref)

    def algorithm(self):
        """
        Update room with created seating

        :return: Updated room
        """

        room = self.room.split(";")
        pref_list = self.pref

        # Lies das doch besser in generator aus und gib das als allgemeine Klassenvariable mit!
        # Jeder anderer algorithmus würde seine preflist ja auch brauchen par random_algo
        # Plus ich habe es so geändert, dass bereits room[1] reingegeben wird, da man das [] ja nicht braucht

        # btw bevor ich es vergesse return room war nur sinnvoll bei rdm algo
        # hier überschreibe den eigenen room der Klasse damit das alles klappt also self.room = new_room

        # Letzte Sache, try catch hier dann doch unnötig, da ich es jetzt immer 1 weiter oben fangen werde
        return room



