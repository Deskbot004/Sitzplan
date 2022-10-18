from logic.algorithms.weighted_algo import WeightedAlgo
import time


class WeightedRandom(WeightedAlgo):
    """
        A function which should try to create an optimized seating but is given a random variable/constraint.

        :param clas: Directory containing the student list
        :param clas_name: Name of the student list/class to be seated as string
        :param room: Room information as string
        :param room_name: Room name as string
        :return: void
    """

    def __init__(self, clas, clas_name, room, room_name):
        super().__init__(clas, clas_name, room, room_name)

    def algorithm(self):
        print("WeightedRandom not implemented yet!")
        time.sleep(3)
        return
