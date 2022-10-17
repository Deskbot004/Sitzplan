import os, time, random, platform
from datetime import date
import classrooms, students, preferences
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = os.path.abspath(os.getcwd())
class_path = path + "/Data/classes/"
room_path =  path + "/Data/rooms/"
seatings_path = path + "/Data/seatings/"
    
    
def show_seatings():
    room_name = input("Room: ")
    clas_name = input("Class: ")
    
    file = open(seatings_path + clas_name + room_name + ".txt", "r")
    room_list = file.read()
    file.close()
    
    semi = room_list.split(";")


    room = []
    for element in semi:
        room.append(element.split(","))
    
    
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
    
show_seatings()