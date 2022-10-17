from logic import LogicMain

'''
Acts as the starting main and activates the main logic remotely.

Functions:
    main()
'''


def main():
    """
    Starts the main logic. Can be later updated to start the GUI.

    :return: void
    """
    LogicMain.start_logic()


if __name__ == "__main__":
    main()
