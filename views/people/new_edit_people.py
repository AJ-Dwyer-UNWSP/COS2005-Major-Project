# Programmer: Andrew Dwyer
# Date: 4/27/22

import tkinter
from data_context import DataContext
from data_models.person import Person
import random
import tkinter.messagebox


class NewEditPeopleView:
    # is_edit_view tells whether the view is used as an edit or a create view
    # on_data_updated is a callback to tell the previous screen to update its data
    # person is the person to edit; it is only needed if used as an edit view
    def __init__(self, data_context: DataContext, is_edit_view, person, on_data_updated):
        # set up data fields
        self.__data_context = data_context
        self.__is_edit_view = is_edit_view
        self.__cur_person = person
        self.__on_data_updated = on_data_updated
        # set __first_name and __last_name
        if is_edit_view:  # then set to the person values passed in
            self.__first_name = person.get_first_name()
            self.__last_name = person.get_last_name()
        else:  # then set to default view
            self.__first_name = ''
            self.__last_name = ''

        # set up window
        self.__main_window = tkinter.Toplevel()
        self.__main_window.title(f"{'Edit' if is_edit_view else 'New'} Person")

        # set up frames
        self.__first_name_frame = tkinter.Frame(self.__main_window)
        self.__last_name_frame = tkinter.Frame(self.__main_window)
        self.__btn_frame = tkinter.Frame(self.__main_window)

        # set up first name frame
        self.__first_name_lbl = tkinter.Label(self.__first_name_frame, text="First Name")
        self.__first_name_entry = tkinter.Entry(self.__first_name_frame)

        # set up last name frame
        self.__last_name_lbl = tkinter.Label(self.__last_name_frame, text="Last Name")
        self.__last_name_entry = tkinter.Entry(self.__last_name_frame)

        # set up bottom btns
        self.__save_btn = tkinter.Button(self.__btn_frame, text="Save", command=self.__save)
        self.__cancel_btn = tkinter.Button(self.__btn_frame, text="Cancel", command=self.__main_window.destroy)

        # pack the elements
        self.__first_name_lbl.pack(side="left")
        self.__first_name_entry.pack(side="left")
        self.__last_name_lbl.pack(side="left")
        self.__last_name_entry.pack(side="left")
        self.__save_btn.pack(side="left")
        self.__cancel_btn.pack(side="left")
        self.__first_name_frame.pack(padx=10, pady=10)
        self.__last_name_frame.pack(padx=10, pady=10)
        self.__btn_frame.pack(padx=10, pady=10, anchor="e")

        # if is in edit mode, then set the value of the entries
        if is_edit_view:
            self.__first_name_entry.insert(0, self.__first_name)
            self.__last_name_entry.insert(0, self.__last_name)

        self.__main_window.mainloop()

    def __save(self):
        # get the values from the entries
        self.__first_name = self.__first_name_entry.get()
        self.__last_name = self.__last_name_entry.get()
        # validate the inputs
        if self.__first_name != '' and self.__last_name != '':  # then the inputs are valid
            if self.__is_edit_view == True:  # then in edit mode and need to update person
                self.__cur_person.set_last_name(self.__last_name)
                self.__cur_person.set_first_name(self.__first_name)
                # update and display a message if the operation failed
                if not self.__data_context.update_person(self.__cur_person):
                    self.__display_error()
            else:  # then in create mode so need to add a new person
                # create an empty person for the user to fill out with a random id
                self.__cur_person = Person(random.randint(0, 9999999), self.__first_name, self.__last_name)
                # create and display a message if the operation failed
                if not self.__data_context.create_person(self.__cur_person):
                    self.__display_error()
            self.__on_data_updated()  # call the callback for the previous screen to update its data
            self.__main_window.destroy()
        else:  # then the inputs weren't valid
            tkinter.messagebox.showinfo("Error", "All fields must be filled out to continue")

    def __display_error(self):
        tkinter.messagebox.showinfo("Error", "There was an error. Please try again.")
