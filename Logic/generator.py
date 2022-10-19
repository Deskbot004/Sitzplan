import os, time, platform
from logic import classrooms, students
from logic.algorithms import random_algo, weighted_optimized, weighted_random, constraint_random

'''
Starts the process of generating the seating.
Right now every algorithm is at least present as a stub.
Current plan is to have a complete random algorithm, a optimized weighted algorithm and
an optimized algorithm with more random elements.

TODO: create simple weighted random algorithm (only constraints) [random_constraint()]

TODO: pretty much everything except complete random

Functions:
    start()
'''

path = os.path.abspath(os.getcwd())
class_path = path + "/data/classes/"
room_path =  path + "/data/rooms/"
seatings_path = path + "/data/seatings/"


def start():
    """
    Function that starts the selection process of the algorithm. In a text based environment.

    :return: void
    """
    if platform.system() == "Linux":
        os.system('clear')
    elif platform.system() == "Windows":
        os.system('cls')
    else:
        print("Unsupported System detected. Please either use Windows or Linux.")
        time.sleep(5)
        return
    
    print("--- Room select ---\nPlease choose one of these rooms: ")
    for file in os.listdir(room_path):
        if file.endswith(".txt"):
            print(file[:-4]+ " |")
    room_name = input ("\nSelection: ")
    room = classrooms.get_classroom(room_name)
    
    print("--- Class select ---\nPlease choose one of these classes: ")
    for file in os.listdir(class_path):
        if file.endswith(".json"):
            print(file[:-5]+ " |")
    clas_name = input("\nSelection: ")
    clas = students.get_student_list(clas_name)
    
    if len(clas) > room.count("1"):
        print("This room does not have enough seating available for the class! Returning to main menu.")
        time.sleep(3)
        return

    running = 1
    error = 0

    while running == 1:
        print(
            "--- Algorithm select ---\nPlease choose the algorithm:\n 1. Complete random\n 2. Random with Constraints\n 3. Weighted optimized\n 4. Weighted random")
        algorithm = input("Selection: ")

        if algorithm == "1":
            room = random_algo.start(clas, clas_name, room, room_name)
            used_algorithm = weighted_random.WeightedRandom(clas, clas_name, room, room_name)
            running = 0
        elif algorithm == "2":
            used_algorithm = constraint_random.ConstraintRandom(clas, clas_name, room, room_name)
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

        used_algorithm.create_image()
        #reader = input("Image created. Type to continue")
        used_algorithm.show_result()
        #reader = input("Result was shown. Type to continue")
        used_algorithm.save_result()
        del used_algorithm
