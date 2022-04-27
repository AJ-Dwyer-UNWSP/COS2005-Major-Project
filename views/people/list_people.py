# Programmer: Andrew Dwyer
# Date: 4/27/22

import tkinter
import tkinter.messagebox
from data_context import DataContext
from data_models.person import Person
from views.people.new_edit_people import NewEditPeopleView


class ListPeopleView:
    def __init__(self, data_context: DataContext):
        # set up fields
        self.__data_context = data_context
        self.__curr_person: Person = Person(1, "1", "1")
        self.__lst_people = self.__data_context.get_people()
        print(self.__lst_people)

        # set up view
        self.__main_window = tkinter.Toplevel()
        self.__main_window.title("People")
        self.__edit_btn = tkinter.Button(self.__main_window, text="Edit", command=self.__edit_person)
        self.__edit_btn.pack(side="left")

    def __new_person(self):
        # open the new person view and set is_edit_view to false and person to None
        NewEditPeopleView(self.__data_context, False, None)

    def __edit_person(self):
        # open the edit view if the current person is not None to avoid an Exception
        if self.__curr_person is not None:
            NewEditPeopleView(self.__data_context, True, self.__curr_person)

    def __delete_curr_person(self):
        # delete the current person if it is not None
        if self.__curr_person is not None:
            # delete the person and show a message if the operation failed
            if not self.__data_context.delete_person(self.__curr_person.get_person_id()):
                self.__display_error()

    def __display_error(self):
        tkinter.messagebox.showinfo("There was an error. Please try again.")
