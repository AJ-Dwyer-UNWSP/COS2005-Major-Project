# Programmer: Andrew Dwyer
# Date: 4/26/22

import tkinter
from views.people.list_people import ListPeopleView


# this is the main view of the application
class MainView:
    def __init__(self, data_context):
        # create a data context
        self.__data_context = data_context

        # set the window up
        self.__main_window = tkinter.Tk()
        self.__main_window.title("Streamlined Service")
        self.__main_window.minsize(600, 300)  # set the minsize the window

        # set up frames
        self.__menu_frame = tkinter.Frame(self.__main_window)  # this is the top frame for the menu buttons
        self.__main_frame = tkinter.Frame(self.__main_window)  # this is the main frame for the content

        # set up and pack menu buttons
        self.__setup_menu_btns()

        # pack the frames
        self.__menu_frame.pack()
        self.__main_frame.pack()

        # start the mainloop
        self.__main_window.mainloop()

    def __setup_menu_btns(self):
        self.__new_service_btn = tkinter.Button(self.__menu_frame, text="New Service")
        self.__delete_service_btn = tkinter.Button(self.__menu_frame, text="Delete Service")
        self.__edit_service_btn = tkinter.Button(self.__menu_frame, text="Edit Service")
        self.__view_roles_btn = tkinter.Button(self.__menu_frame, text="View Roles")
        self.__view_people_btn = tkinter.Button(self.__menu_frame, text="View People", command=self.__view_people)
        self.__quit_btn = tkinter.Button(self.__menu_frame, text="Quit", command=self.__main_window.destroy)

        # pack the buttons
        self.__new_service_btn.pack(side="left")
        self.__delete_service_btn.pack(side="left")
        self.__edit_service_btn.pack(side="left")
        self.__view_roles_btn.pack(side="left")
        self.__view_people_btn.pack(side="left")
        self.__quit_btn.pack(side="left")

    def __new_service(self):
        # navigate to the new service view
        pass

    def __edit_service(self):
        # navigate to the edit service view
        pass

    def __delete_service(self):
        # delete service
        # set new current service
        pass

    def __view_roles(self):
        # navigate to the view roles
        pass

    def __view_people(self):
        ListPeopleView(self.__data_context)

    def __service_clicked(self):
        # change the current service
        pass

    def __set_curr_service(self):
        # set data context
        # update UI
        pass

    def __add_participant(self):
        pass

    def __edit_participant(self):
        pass

