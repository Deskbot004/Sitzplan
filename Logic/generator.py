import os, time, random, platform
from datetime import date
from logic import classrooms, students, preferences
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = os.path.abspath(os.getcwd())
class_path = path + "/data/classes/"
room_path =  path + "/data/rooms/"
seatings_path = path + "/data/seatings/"


def start():
    if platform.system() == "Linux":
        os.system('clear')
    elif platform.system() == "Windows":
        os.system('cls')
    else:
        print("Unsupported System detected. Please either use Windows or Linux.")
        time.sleep(5)
        return
    
    print("--- Algorithm select ---\nPlease choose the algorithm:\n 1. Complete Random\n 2. Weighted\n 3. Weighted radom")
    algorithm = input("Selection: ")
    
    print("--- Room select ---\nPlease choose one of these rooms: ")
    for file in os.listdir(room_path):
        if file.endswith(".txt"):
            print(file.removesuffix(".txt") + "| ", end= ' ')
    room_name = input ("\nSelection: ")
    room = classrooms.get_classroom(room_name)
    
    print("--- Class select ---\nPlease choose one of these classes: ")
    for file in os.listdir(class_path):
        if file.endswith(".json"):
            print(file.removesuffix(".json") + "| ", end= ' ')
    clas_name = input("\nSelection: ")
    clas = students.get_student_list(clas_name)
    
    if len(clas) > room.count("1"):
        print("This room does not have enough seatings for the class! Returning to main menu.")
        time.sleep(3)
        return
    
    if algorithm == "1":
        random_algo(clas, clas_name, room, room_name)
    elif algorithm == "2":
        weighted_algo(clas, clas_name, room, room_name)
    elif algorithm == "3":
        weighted_r_algo(clas, clas_name, room, room_name)
    elif algorithm.lower() == "q" or algorithm.lower() == "quit":
        return
    else:
        print("Please select a valid algorithm. Returning to main menu.")
        time.sleep(3)

# A completely random algorithm, which assigns any seating to any student. For the best results use rooms with the same number of students as seatings
def random_algo(clas, clas_name, room, room_name):
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
        
    #for row in room:
    #    print(row)
    
    fig, ax = plt.subplots()
    
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    
    # expects each room to be at least 2 spaces wide
    info_arr = [ "" for x in range(len(room[0]))]
    info_arr[0] = "Class: " + clas_name
    info_arr[len(room[0]) - 1] = "Room: " + room_name
    
    df = pd.DataFrame(np.array(room), columns=info_arr)
    
    ax.table(cellText=df.values, colLabels=df.columns, loc='center')
    fig.tight_layout()
    plt.savefig(seatings_path + clas_name + "_" + room_name + "_" + str(date.today()) + ".png", dpi = 300)
    plt.show() # pip install pyqt5
    
    # save seatings
    try:
        file = open(seatings_path+clas_name+room_name+ ".txt", "x")
    except FileExistsError:
        file = open(seatings_path+clas_name+room_name+".txt", "w")    
    
    action = input("Press any key to continue or \"a\" to try again: ")
    
    if action == "a":
        random_algo(old_clas, clas_name, old_room, room_name)
        return
    else:
        print("Image saved in "+ seatings_path+ ". Returning to main menu.")
        
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
                                
    
def weighted_algo(clas, clas_name, room, room_name):
    if platform.system() == "Linux":
        os.system('clear')
    elif platform.system() == "Windows":
        os.system('cls')
    else:
        print("Unsupported System detected. Please either use Windows or Linux.")
        time.sleep(5)
        return
    
    print(" --- Weighted algorithm ---\nPlease choose an option.\n 1: Use an existing preference list\n 2: Create a new one\n 3: Edit an existing one\n 4: Delete a preference list\n 5: Return")
    action = input("Chosen option: ")
    
    while 1:
        if action == "1":
            print("not implemented yet")
            time.sleep(3)
        elif action == "2":
            preferences.preferences_create(clas, clas_name)
            return
        elif action == "3":
            print("not implemented yet")
            time.sleep(3)
        elif action == "4":
            print("not implemented yet")
            time.sleep(3)
        elif action.lower() == "quit" or action.lower() == "q" or action == "5":
            return
        else:
            print("Please choose an existing option.")
            time.sleep(3)
            
def weighted_r_algo(clas, room):
    print("not implemented yet")
    time.sleep(3)