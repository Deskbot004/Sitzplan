import os, time, platform
from logic import classrooms, students, preferences
from logic.algorithms import random_algo, weighted_optimized, weighted_random, constraint_random

'''
Starts the process of generating the seating.
Right now every algorithm is at least present as a stub.
Current plan is to have a complete random algorithm, a optimized weighted algorithm and
an optimized algorithm with more random elements.

TODO: create simple weighted random algorithm (only constraints) [random_constraint()]

TODO: pretty much everything except complete random

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!! SHOULD LATER NOT BE ACCESSED ANYMORE SINCE STARTWEB SHOULD REPLACES EVERY FUNCTIONALITY PRESENT HERE !!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Functions:
    start()
'''

path = os.path.abspath(os.getcwd())
class_path = path + "/data/classes/"
room_path = path + "/data/rooms/"
seatings_path = path + "/data/seatings/"
pref_path = path + "/data/preferences/"


def start():
    """
    Function that starts the selection process of the algorithm. In a text based environment.

    :return: void
    """
    room_name = "3Row"
    room_ret = classrooms.get_classroom(room_name)  # check room[1] for FAIL
    room = room_ret[0].split(";")

    clas_name = "10Names"
    clas_ret = students.get_student_list(clas_name)
    clas = clas_ret[0]

    pref_ret = preferences.preferences_read(clas_name)  #Teilt sich ja den namen
    pref = pref_ret[0]

    """
    if len(clas) > room.count("1"):
        print("This room does not have enough seating available for the class! Returning to main menu.")
        time.sleep(3)
        return
    """
    running = 1
    error = 0

    while running == 1:
        print(
            "--- Algorithm select ---\nPlease choose the algorithm:\n 1. Complete random\n 2. Random with Constraints\n"
            " 3. Weighted optimized\n 4. Weighted random")
        algorithm = input("Selection: ")

        if algorithm == "2":
            used_algorithm = constraint_random.ConstraintRandom(clas, clas_name, room, room_name, pref)
            error = used_algorithm.startup()
            running = 0
        elif algorithm == "3":
            used_algorithm = weighted_optimized.WeightedOptimized(clas, clas_name, room, room_name)
            error = used_algorithm.startup()
            running = 0
        elif algorithm == "4":
            used_algorithm = weighted_random.WeightedRandom(clas, clas_name, room, room_name)
            error = used_algorithm.startup()
            running = 0
        elif algorithm.lower() == "q" or algorithm.lower() == "quit":
            return
        else:
            print("Please select a valid algorithm.")
            time.sleep(3)
            continue

        if error == -1:
            return

        """
        used_algorithm.create_image()
        # reader = input("Image created. Type to continue")
        used_algorithm.show_result()
        # reader = input("Result was shown. Type to continue")
        used_algorithm.save_result()
        del used_algorithm
        """


def run(data):
    """
    New function to be used by the web interface.

    TODO severly outdated!! for every file format

    :param data: String information from website in form of 3 entries
    :return: State of function
    """
    try:
        information = data.split(",")
        #clas_name = information[0]
        clas_name = "10Names"
        room_name = information[1]
        action = information[2]

        room_ret = classrooms.get_classroom(room_name)  # check room[1] for FAIL
        room = room_ret[0].split(";")
        print(room)

        clas_ret = students.get_student_list(clas_name)
        clas = clas_ret[0]
        print(clas)

        pref_ret = preferences.preferences_read(clas_name)
        pref = pref_ret[0]
        print(pref)

        if room_ret[1] == "FAIL" or clas_ret[1] == "FAIL" or pref_ret[1] == "FAIL":
            raise Exception('Getting information failed')

        if action == "show":
            # maybe just return here and give back information of the image to open?
            # used_algorithm = constraint_random.ConstraintRandom(clas, clas_name, room, room_name, pref)
            return
        elif action == "random_algo":
            room = random_algo.start(clas, room)
            used_algorithm = constraint_random.ConstraintRandom(clas, clas_name, room, room_name, pref)
        elif action == "constraint_random":
            used_algorithm = constraint_random.ConstraintRandom(clas, clas_name, room, room_name, pref)
            used_algorithm.startup()
        else:
            raise Exception('No valid action found')

        used_algorithm.create_image()
        # reader = input("Image created. Type to continue")
        # used_algorithm.show_result()
        # reader = input("Result was shown. Type to continue")
        filename = used_algorithm.save_result()
        del used_algorithm
        return filename, "SUCCESS"
    except Exception as error:
        print('Caught this error: ' + repr(error))
        return "", "FAIL"
