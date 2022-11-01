import os, random

'''
Module only containing the algorithm to create a completely random seating.
The seating is shown as an image and saved as a .txt and .png file.

TODO: this Module can easily make use of the new weighted_algo class

Functions:
    start(dictionary, string, string, string)
'''


path = os.path.abspath(os.getcwd())
seatings_path = path + "/data/seatings/"


def start(clas, room):
    """
    A completely random algorithm, which assigns any seating to any student.
    For the best results use rooms with the same number of students as seating available.
    The seating is displayed and saved as an image and can be remade on the spot.
    Also it is then saved as a .txt file to later read and display it.

    :param clas: Dictionary containing the student list
    :param room: Room information as string
    :return: void
    """
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
                room[row_val][col_val] = "---"
            elif room[row_val][col_val] == 0:
                room[row_val][col_val] = ""
            elif room[row_val][col_val] == 3:
                room[row_val][col_val] = "Teacher desk"
            col_val += 1
        row_val += 1

    return room
