import time, os
import students, classrooms, generator

def main():
    running = 1
    
    while running == 1:
        os.system('clear')
        print("--- Main menu --- \nChoose your action: \n 1: Save a new studentslist \n 2: Edit a studentslist\n 3: Create a classroom \n 4: Edit a classroom \n 5: Generate a new seatingslist \n 6: Delete a studentslist \n 7: Delete a classroom \n 8: Close the program")
        user_num = input("Chosen action: ")
        
        if user_num == "1":
            students.save_students()
        elif user_num == "2":
            students.edit_students()
        elif user_num == "3":
            classrooms.create_classroom()
        elif user_num == "4":
            classrooms.edit_classroom()
        elif user_num == "5":
            generator.start()
        elif user_num == "6":
            students.delete_students()
        elif user_num == "7":
            classrooms.delete_classroom()
        elif user_num == "8" or user_num.lower() == "quit" or user_num.lower() == "q":
            running = 0
        else:
            print("Please enter a valid number! Returning to Main menu in 3 secconds.")
            time.sleep(3)

if __name__ == "__main__":
    main()
    
 