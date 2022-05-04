# Programmer: Andrew Dwyer
# Date: 5/3/22

import tkinter
import tkinter.messagebox
from data_context import DataContext
from views.roles.new_edit_role import NewEditRolesView
import tkinter.messagebox


class ListRolesView:
    def __init__(self, data_context: DataContext, update_data):
        # set up fields
        self.__data_context = data_context
        self.__lst_roles = self.__data_context.get_roles()
        self.__curr_role = None
        self.__update_parent_data = update_data

        # set up view
        self.__main_window = tkinter.Toplevel()
        self.__main_window.title("Roles")

        # setup frames
        self.__list_roles_frame = tkinter.Frame(self.__main_window)
        self.__btns_frame = tkinter.Frame(self.__main_window)

        # set up list view
        self.__list_roles_var = tkinter.StringVar()
        self.__list_roles_var.set(self.__lst_roles)
        self.__list_roles_box = tkinter.Listbox(self.__list_roles_frame, listvariable=self.__list_roles_var)
        # bind to the event that an item is clicked in the listbox
        self.__list_roles_box.bind("<<ListboxSelect>>", self.__on_listbox_item_click)
        # create the scrollbar
        self.__scroll_bar = tkinter.Scrollbar(self.__list_roles_frame, orient=tkinter.VERTICAL,
                                              command=self.__list_roles_box.yview)
        # set the listbox to set the scroll bar when it moves
        self.__list_roles_box.config(yscrollcommand=self.__scroll_bar.set)

        # set up btns
        self.__new_btn = tkinter.Button(self.__btns_frame, text="New", command=self.__new_role)
        self.__edit_btn = tkinter.Button(self.__btns_frame, text="Edit", command=self.__edit_role)
        self.__delete_btn = tkinter.Button(self.__btns_frame, text="Delete", command=self.__delete_curr_role)
        self.__cancel_btn = tkinter.Button(self.__btns_frame, text="Cancel", command=self.__main_window.destroy)

        # pack elements
        self.__list_roles_box.pack(side="left")
        self.__scroll_bar.pack(side="right", fill=tkinter.Y)
        self.__new_btn.pack(side="left")
        self.__edit_btn.pack(side="left")
        self.__delete_btn.pack(side="left")
        self.__cancel_btn.pack(side="left")

        self.__list_roles_frame.pack(padx=10, pady=10)
        self.__btns_frame.pack(padx=10, pady=10)

    # this happens when an item in the listbox is selected
    def __on_listbox_item_click(self, event):
        try:
            index = self.__list_roles_box.curselection()
            self.__curr_role = self.__lst_roles[index[0]]
        except IndexError:
            self.__curr_role = None

    def __new_role(self):
        # open the new role view and set is_edit_view to false and role to None
        NewEditRolesView(self.__data_context, False, None, self.__update_data)

    def __edit_role(self):
        # open the edit view if the current role is not None to avoid an Exception
        if self.__curr_role is not None:
            NewEditRolesView(self.__data_context, True, self.__curr_role, self.__update_data)
        else:
            tkinter.messagebox.showinfo("Error", "Please select an item before performing your operation.")

    def __delete_curr_role(self):
        # delete the current role if it is not None
        if self.__curr_role is not None:
            # delete the role and show a message if the operation failed
            if self.__data_context.delete_role(self.__curr_role):
                self.__update_data()
            else:
                self.__display_error()
        else:
            tkinter.messagebox.showinfo("Error", "Please select an item before performing your operation.")

    def __display_error(self):
        tkinter.messagebox.showinfo("Error", "There was an error. Please try again.")

    # this is passed as a callback to the new_edit_roles view; this executes when the new edit view makes an update
    def __update_data(self):
        self.__lst_roles = self.__data_context.get_roles()
        self.__list_roles_var.set(self.__lst_roles)
        self.__update_parent_data()
