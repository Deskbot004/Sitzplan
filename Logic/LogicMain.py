import time, os, platform
from logic import students, generator

'''
Starts the logic in a text based environment.

Functions:
    start_logic()
'''


def start_logic():
    """
    Function starts the text based selection for the user. Should be later replaced by GUI.

    :return: void
    """
    running = 1
    
    # Main loop for user selection
    while running == 1:
        if platform.system() == "Linux":
            os.system('clear')
        elif platform.system() == "Windows":
            os.system('cls')
        print("--- Main menu --- \nChoose your action: \n5: Generate a new seating list \n 8: Close the program")
        user_num = input("Chosen action: ")
        
        if user_num == "5":
            generator.start()
        elif user_num == "8" or user_num.lower() == "quit" or user_num.lower() == "q":
            running = 0
        else:
            print("Please enter a valid number! Returning to Main menu in 3 seconds.")
            time.sleep(3)
 