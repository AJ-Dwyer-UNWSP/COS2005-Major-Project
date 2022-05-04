# Programmer: Andrew Dwyer
# Date: 5/3/22

import tkinter
from data_context import DataContext
from data_models.service import Service
import random
import tkinter.messagebox


class NewEditServiceView:
    # is_edit_view tells whether the view is used as an edit or a create view
    # on_data_updated is a callback to tell the previous screen to update its data
    # service is the service to edit; it is only needed if used as an edit view
    def __init__(self, data_context: DataContext, is_edit_view, service, on_data_updated):
        # set up data fields
        self.__data_context = data_context
        self.__is_edit_view = is_edit_view
        self.__cur_service = service
        self.__on_data_updated = on_data_updated
        if is_edit_view:  # then set to the service values passed in
            self.__service_name = service.get_service_name()
            self.__desc = service.get_description()
            self.__datetime = service.get_start_datetime()
        else:  # then set to default view
            self.__service_name = ''
            self.__desc = ''
            self.__datetime = ''

        # set up window
        self.__main_window = tkinter.Toplevel()
        self.__main_window.title(f"{'Edit' if is_edit_view else 'New'} Service")

        # set up frames
        self.__service_name_frame = tkinter.Frame(self.__main_window)
        self.__desc_frame = tkinter.Frame(self.__main_window)
        self.__datetime_frame = tkinter.Frame(self.__main_window)
        self.__btn_frame = tkinter.Frame(self.__main_window)

        # set up service name frame
        self.__service_name_lbl = tkinter.Label(self.__service_name_frame, text="Service Name")
        self.__service_name_entry = tkinter.Entry(self.__service_name_frame)

        # set up description frame
        self.__desc_lbl = tkinter.Label(self.__desc_frame, text="Description")
        self.__desc_entry = tkinter.Entry(self.__desc_frame)

        # set up datetime frame
        self.__datetime_lbl = tkinter.Label(self.__datetime_frame, text="Start Date and Time")
        self.__datetime_entry = tkinter.Entry(self.__datetime_frame)

        # set up bottom btns
        self.__save_btn = tkinter.Button(self.__btn_frame, text="Save", command=self.__save)
        self.__cancel_btn = tkinter.Button(self.__btn_frame, text="Cancel", command=self.__main_window.destroy)

        # pack the elements
        self.__service_name_lbl.pack(side="left")
        self.__service_name_entry.pack(side="left")
        self.__desc_lbl.pack(side="left")
        self.__desc_entry.pack(side="left")
        self.__datetime_lbl.pack(side="left")
        self.__datetime_entry.pack(side="left")
        self.__save_btn.pack(side="left")
        self.__cancel_btn.pack(side="left")
        self.__service_name_frame.pack(padx=10, pady=10)
        self.__desc_frame.pack(padx=10, pady=10)
        self.__datetime_frame.pack(padx=10, pady=10)
        self.__btn_frame.pack(padx=10, pady=10, anchor="e")

        # if is in edit mode, then set the value of the entries
        if is_edit_view:
            self.__service_name_entry.insert(0, self.__service_name)
            self.__desc_entry.insert(0, self.__desc)
            self.__datetime_entry.insert(9, self.__datetime)

        self.__main_window.mainloop()

    def __save(self):
        # get the values from the entries
        self.__service_name = self.__service_name_entry.get()
        self.__desc = self.__desc_entry.get()
        self.__datetime = self.__datetime_entry.get()
        # validate the inputs
        if self.__service_name != '' and self.__desc != '' and self.__datetime != '':  # then the inputs are valid
            if self.__is_edit_view == True:  # then in edit mode and need to update service
                self.__cur_service.set_description(self.__desc)
                self.__cur_service.set_service_name(self.__service_name)
                self.__cur_service.set_start_datetime(self.__datetime)
                # update and display a message if the operation failed
                if not self.__data_context.update_service(self.__cur_service):
                    self.__display_error()
            else:  # then in create mode so need to add a new service
                # create an empty service for the user to fill out with a random id
                self.__cur_service = Service(random.randint(0, 9999999), self.__datetime, self.__service_name, self.__desc)
                # create and display a message if the operation failed
                if not self.__data_context.create_service(self.__cur_service):
                    self.__display_error()
            self.__on_data_updated()  # call the callback for the previous screen to update its data
            self.__main_window.destroy()
        else:  # then the inputs weren't valid
            tkinter.messagebox.showinfo("Error", "All fields must be filled out to continue")

    def __display_error(self):
        tkinter.messagebox.showinfo("Error", "There was an error. Please try again.")
