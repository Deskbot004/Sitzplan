from logic.algorithms.weighted_algo import WeightedAlgo
import logic.algorithms.random_algo as ran_alg
from logic import preferences as pref
import math
import numpy as np


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

    @staticmethod
    def get_key_from_value(dictionary, val):
        keys = [k for k, v in dictionary.items() if v == val]
        if keys:
            return keys[0]
        return None

    @staticmethod
    def neighbors(a, radius, row_number, column_number):
        return [[a[i][j] if 0 <= i < len(a) and 0 <= j < len(a[0]) else 0
                for j in range(column_number - 1 - radius, column_number + radius)]
                for i in range(row_number - 1 - radius, row_number + radius)]

    def algorithm(self):
        """
        Update room with created seating

        :return: Updated room
        """

        epochs = 1000
        FRONT_SEAT_SCORE = 2
        NO_NEGATIVE_NEIGHBOR_SCORE = 1
        format_room = self.room[:]
        format_room.reverse()   # reversed because the last element in format_room is the first row!

        seatable_rows = [i for i, row in zip(range(len(format_room)), format_room) if "1" in row]
        # front_end_seatable = math.ceil(len(seatable_rows) * 0.3) - 1
        front_end_total = seatable_rows[math.ceil(len(seatable_rows) * 0.3)] - 1
        front_preferred_students = [student for student in self.pref.keys() if self.pref[student][4] != "empty"]
        # negative_preferred_students = [student for student in self.pref.keys() if self.pref[student][3] != "empty"]

        THEORETICAL_OPT_SCORE = NO_NEGATIVE_NEIGHBOR_SCORE * len(self.clas.keys()) \
                                + FRONT_SEAT_SCORE * len(front_preferred_students)
        rooms = []
        scores = []
        for epoch in range(epochs):
            total_score = 0
            rand_room = ran_alg.start(self.clas, self.room[:])
            rand_room.reverse()
            if rand_room in rooms:
                print("DUPLICATE ROOM")
                continue

            for row_count, row in zip(range(len(rand_room)), rand_room):
                for seat_count, student in zip(range(len(row)), row):
                    if student in list(self.clas.values()):
                        # check for front preference
                        student_key = self.get_key_from_value(self.clas, student)
                        if row_count <= front_end_total and student_key \
                           in front_preferred_students:
                            total_score += FRONT_SEAT_SCORE

                        # check for negative preference
                        neighbors = [student for student in
                                np.asarray(self.neighbors(rand_room, 1, row_count + 1, seat_count + 1)).flatten().tolist()
                                if student != "" and student != "0" and student != "---" and student != "Teacher desk"]
                        neighbor_keys = [self.get_key_from_value(self.clas, neighbor) for neighbor in neighbors]

                        if self.pref[student_key][3] not in neighbor_keys:
                            total_score += NO_NEGATIVE_NEIGHBOR_SCORE
            rooms.append(rand_room)
            scores.append(total_score)

        # get a room with highest score
        max_index = scores.index(max(scores))
        good_room = rooms[max_index]
        good_room.reverse()
        print(f"The found room has a score of {scores[max_index]} out of {THEORETICAL_OPT_SCORE}.")
        print(good_room)
        return good_room



