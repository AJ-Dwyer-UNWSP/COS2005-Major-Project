# Programmer: Andrew Dwyer
# Date: 4/27/22

import tkinter
from data_context import DataContext
from data_models.person import Person
import random


class NewEditPeopleView:
    # is_edit_view tells whether the view is used as an edit or a create view
    # person is the person to edit; it is only needed if used as an edit view
    def __init__(self, data_context: DataContext, is_edit_view, person):
        # set up data fields
        self.__data_context = data_context
        self.__is_edit_view = is_edit_view
        self.__cur_person = person
        self.__first_name = ''
        self.__last_name = ''
        print(self.__cur_person)

        # set up window
        self.__main_window = tkinter.Toplevel()
        self.__main_window.title(f"{'Edit' if is_edit_view else 'New'} Person")

    def __save(self):
        # validate the inputs
        if self.__first_name != '' and self.__last_name != '':  # then the inputs are valid
            # create an empty person for the user to fill out with a random id
            self.__cur_person = Person(random.randint(0, 9999999), self.__first_name, self.__last_name)

            if self.__is_edit_view == True:  # then in edit mode and need to update person
                # update and display a message if the operation failed
                if not self.__data_context.update_person(self.__cur_person):
                    self.__display_error()
            else:  # then in create mode so need to add a new person
                # create and display a message if the operation failed
                if not self.__data_context.create_person(self.__cur_person):
                    self.__display_error()
        else:  # then the inputs weren't valid
            tkinter.messagebox.showinfo("All fields must be filled out to continue")

    def __display_error(self):
        tkinter.messagebox.showinfo("There was an error. Please try again.")
