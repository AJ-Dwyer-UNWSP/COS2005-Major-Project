# Programmer: Andrew Dwyer
# Date: 5/3/22

import tkinter
from data_context import DataContext
from data_models.role import Role
import random
import tkinter.messagebox


class NewEditRolesView:
    # is_edit_view tells whether the view is used as an edit or a create view
    # on_data_updated is a callback to tell the previous screen to update its data
    # role is the role to edit; it is only needed if used as an edit view
    def __init__(self, data_context: DataContext, is_edit_view, role, on_data_updated):
        # set up data fields
        self.__data_context = data_context
        self.__is_edit_view = is_edit_view
        self.__cur_role = role
        self.__on_data_updated = on_data_updated
        # set __role_name
        if is_edit_view:  # then set to the role values passed in
            self.__role_name = role.get_role_name()
        else:  # then set to default view
            self.__role_name = ''

        # set up window
        self.__main_window = tkinter.Toplevel()
        self.__main_window.title(f"{'Edit' if is_edit_view else 'New'} Role")

        # set up frames
        self.__role_name_frame = tkinter.Frame(self.__main_window)
        self.__btn_frame = tkinter.Frame(self.__main_window)

        # set up role name frame
        self.__role_name_lbl = tkinter.Label(self.__role_name_frame, text="Role Name")
        self.__role_name_entry = tkinter.Entry(self.__role_name_frame)

        # set up bottom btns
        self.__save_btn = tkinter.Button(self.__btn_frame, text="Save", command=self.__save)
        self.__cancel_btn = tkinter.Button(self.__btn_frame, text="Cancel", command=self.__main_window.destroy)

        # pack the elements
        self.__role_name_lbl.pack(side="left")
        self.__role_name_entry.pack(side="left")
        self.__save_btn.pack(side="left")
        self.__cancel_btn.pack(side="left")
        self.__role_name_frame.pack(padx=10, pady=10)
        self.__btn_frame.pack(padx=10, pady=10, anchor="e")

        # if is in edit mode, then set the value of the entries
        if is_edit_view:
            self.__role_name_entry.insert(0, self.__role_name)

        self.__main_window.mainloop()

    def __save(self):
        # get the values from the entries
        self.__role_name = self.__role_name_entry.get()
        # validate the inputs
        if self.__role_name != '' and self.__role_name != '':  # then the inputs are valid
            if self.__is_edit_view == True:  # then in edit mode and need to update role
                self.__cur_role.set_role_name(self.__role_name)
                # update and display a message if the operation failed
                if not self.__data_context.update_role(self.__cur_role):
                    self.__display_error()
            else:  # then in create mode so need to add a new role
                # create an empty role for the user to fill out with a random id
                self.__cur_role = Role(random.randint(0, 9999999), self.__role_name)
                # create and display a message if the operation failed
                if not self.__data_context.create_role(self.__cur_role):
                    self.__display_error()
            self.__on_data_updated()  # call the callback for the previous screen to update its data
            self.__main_window.destroy()
        else:  # then the inputs weren't valid
            tkinter.messagebox.showinfo("Error", "All fields must be filled out to continue")

    def __display_error(self):
        tkinter.messagebox.showinfo("Error", "There was an error. Please try again.")
