import os, time, random
from datetime import date
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
Module only containing the algorithm to create a completely random seating.
The seating is shown as an image and saved as a .txt and .png file.

Functions:
    start(dictionary, string, string, string)
'''


path = os.path.abspath(os.getcwd())
seatings_path = path + "/data/seatings/"


def start(clas, clas_name, room, room_name):
    """
    A completely random algorithm, which assigns any seating to any student.
    For the best results use rooms with the same number of students as seating available.
    The seating is displayed and saved as an image and can be remade on the spot.
    Also it is then saved as a .txt file to later read and display it.

    :param clas: Directory containing the student list
    :param clas_name: Name of the student list/class to be seated as string
    :param room: Room information as string
    :param room_name: Room name as string
    :return: void
    """
    old_room = room
    old_clas = clas
    room = room.split(";")

    row = 0
    for line in room:
        new_row = []
        for char in line:
            new_row.append(int(char))
        room[row] = new_row
        row += 1

    values = []
    for val in clas.keys():
        values.append(val)

    while len(values) > 0:
        rand_row = random.randrange(len(room))
        rand_col = random.randrange(len(room[rand_row]))
        if room[rand_row][rand_col] == 1:
            rand_stud = random.randrange(len(values))
            room[rand_row][rand_col] = clas[values[rand_stud]]
            values.remove(values[rand_stud])

    row_val = 0
    for row in room:
        col_val = 0
        for col in row:
            if room[row_val][col_val] == 1 or room[row_val][col_val] == 2:
                room[row_val][col_val] = "Empty"
            elif room[row_val][col_val] == 0:
                room[row_val][col_val] = ""
            elif room[row_val][col_val] == 3:
                room[row_val][col_val] = "Teacher desk"
            col_val += 1
        row_val += 1

    fig, ax = plt.subplots()

    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    # expects each room to be at least 2 spaces wide
    info_arr = ["" for x in range(len(room[0]))]
    info_arr[0] = "Class: " + clas_name
    info_arr[len(room[0]) - 1] = "Room: " + room_name

    df = pd.DataFrame(np.array(room), columns=info_arr)

    ax.table(cellText=df.values, colLabels=df.columns, loc='center')
    fig.tight_layout()
    plt.savefig(seatings_path + clas_name + "_" + room_name + "_" + str(date.today()) + ".png", dpi=300)
    plt.show()  # pip install pyqt5

    # save seatings
    try:
        file = open(seatings_path + clas_name + room_name + ".txt", "x")
    except FileExistsError:
        file = open(seatings_path + clas_name + room_name + ".txt", "w")

    action = input("Press any key to continue or \"a\" to try again: ")

    if action == "a":
        start(old_clas, clas_name, old_room, room_name)
        return
    else:
        print("Image saved in " + seatings_path + ". Returning to main menu.")

        room_list = ""
        for element in room:
            for name in element:
                room_list += name + ","
            room_list = room_list[:-1]
            room_list += ";"
        room_list = room_list[:-1]

        file.write(room_list)
        file.close()
        time.sleep(5)
        return
