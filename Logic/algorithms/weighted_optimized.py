from logic.algorithms.weighted_algo import WeightedAlgo
import time


class WeightedOptimized(WeightedAlgo):
    """
        A function which should later create an optimized version of the seating.
        It is also the only access to the preference lists right now.

        :param clas: Directory containing the student list
        :param clas_name: Name of the student list/class to be seated as string
        :param room: Room information as string
        :param room_name: Room name as string
        :return: void
    """

    def __init__(self, clas, clas_name, room, room_name):
        super().__init__(clas, clas_name, room, room_name)

    def algorithm(self):
        print("WeightedOptimized not implemented yet!")
        time.sleep(3)
        return
