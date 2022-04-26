# Programmer: Andrew Dwyer
# Date: 4/26/22

import tkinter


# this is the main view of the application
class MainView:
    def __init__(self):
        # set the window up
        self.__main_window = tkinter.Tk()
        self.__main_window.title("Streamlined Service")
        self.__main_window.mainloop()
