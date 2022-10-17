import os, time, json, platform

#Biggest TODO

path = os.path.abspath(os.getcwd())
pref_path = path + "/Data/preferences/"

def preferences_create(clas, clas_name):
    clear_screen()
    print("--- Create a new preference list ---")
    
    pref_dict = {}
    
    try:
        file = open(pref_path + clas_name + ".json", "x")
        file.close()
    except FileExistsError:
        print("Preference list does already exist. Either edit or delete.")
        time.sleep(3)
        return
    
    for studentnr in clas:
        clear_screen()
        print("Use the format with the listed studentnumbers or 0's if no preference exists for x1 to x3: x1;x2;x3;y;z.\n x1: 1. Partner\n x2: 2. Partner\n x3: 3. Partner\n y: Should not be Partner (signaled by negative number)\n z: \"front\" or \"back\"\n y and z are optional(e.g. \"1;12;3;-9;front\" or \"3;4;7;back\")")
        for student in clas.items():
            print(student)
        new_pref = input("Please enter the preferences for " + str(clas[studentnr])+ ": ")
        pref_dict[studentnr] = new_pref
    
    file = open(pref_path + clas_name + ".json", "w")
    json.dump(pref_dict, file)
    file.close()
    return
    
    
def preferences_edit():
    clear_screen()
    print("not implemented yet")
    time.sleep(3)
    
def preferences_delete():
    clear_screen()
    print("not implemented yet")
    time.sleep(3)
    
    
def preferences_read():
    print("not implemented yet")
    time.sleep(3)
    
def validate_entry(entry, studentnr):
    entry = entry.split()
    return
    
# i dont know why i was to lazy to implement this until now    
def clear_screen():
    if platform.system() == "Linux":
        os.system('clear')
    elif platform.system() == "Windows":
        os.system('cls')
    else:
        print("Unsupported System detected. Please either use Windows or Linux.")
        time.sleep(5)
        return