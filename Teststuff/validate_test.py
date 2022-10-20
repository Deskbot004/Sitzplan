test_valid1 = "1;2;3;-4;front"
test_valid2 = "1;2;0"
test_valid3 = "0"
test_valid4 = "0;-2"
test_valid5 = "0;front"
test_invalid0 = ""
test_invalid1 = "5;2;3"
test_invalid2 = "1;0;3"
test_invalid3 = "-1;2;3"
test_invalid4 = "1;2;3;4"
test_invalid5 = "1;2;3;-4;front;3"
test_invalid6 = "-2"
test_invalid7 = "front"
test_invalid8 = "0-2"
test_invalid9 = "0;-5"

valids = (test_valid1, test_valid2, test_valid3, test_valid4, test_valid5)
invalids = (test_invalid0, test_invalid1, test_invalid2, test_invalid3, test_invalid4, test_invalid5, test_invalid6, test_invalid7, test_invalid8, test_invalid9)

def validate(studentnr, entry):
    to_validate = entry.split(";")

    print(to_validate)

    if not to_validate:
        print("List is empty!")
        return False
    elif studentnr in to_validate or "-" + studentnr in to_validate:
        print("Student contained in own preferences!")
        return False
    elif not to_validate[0].isdigit():
        print("No starting Zero!")
        return False
    elif int(to_validate[0]) < 0:
        print("No starting Zero!")
        return False

    pos_pref = 0
    for pref in to_validate:
        if pos_pref == -1:
            if not check_int(pref):
                pos_pref = -2
            elif int(pref) >= 0:
                print("Positive preference after no more allowed!")
                return False
            else:
                pos_pref = -2
        elif pos_pref == -2:
            print("Position statement should be end of preference!")
            return False
        elif not check_int(pref):
            pos_pref = -2
        elif int(pref) <= 0:
            pos_pref = -1
        elif pos_pref > 2:
            print("Positive preference after no more allowed!")
            return False
        else:
            pos_pref = pos_pref + 1

    return True


def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

'''
for test in valids:
    print(validate("5", test))

print("__________________________________")
for test in invalids:
    print(validate("5", test))
'''


def editing():
    pref_dict = {"1": "0", "2": "0", "3": "0", "4": "0", "5": "0", "6": "0", "7": "0", "8": "0", "9": "0", "10": "0"}
    student_dict = {"1": "Liam", "2": "Olivia", "3": "Noah", "4": "Emma", "5": "Oliver", "6": "Charlotte", "7": "Elijah",
                    "8": "Amelia", "9": "James", "10": "Ava"}

    while 1:
        print("--- Editing a preference list ---\nEither change the preference or quit with \"done\".")
        for elem in student_dict.keys():
            print(elem + ". " + student_dict[elem] + ": " + pref_dict[elem])

        student = input("Please enter the number of the student which preferences should be changed: ")

        if student.lower() == "done" or student.lower() == "quit" or student.lower() == "q":
            return

        pref = input("Please enter the new preferences for the student " + student_dict[student] + ": ")
        if not validate(student, pref):
            print("Please enter a valid preference!")
        else:
            pref_dict[student] = pref


editing()
