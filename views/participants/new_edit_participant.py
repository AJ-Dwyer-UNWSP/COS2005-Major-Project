# Programmer: Andrew Dwyer
# Date: 5/3/22

import tkinter
from data_context import DataContext
from data_models.participant import Participant
import tkinter.messagebox


class NewEditParticipantView:
    # is_edit_view tells whether the view is used as an edit or a create view
    # on_data_updated is a callback to tell the previous screen to update its data
    # participant is the participant to edit; it is only needed if used as an edit view
    def __init__(self, data_context: DataContext, is_edit_view, participant, on_data_updated):
        # set up data fields
        self.__data_context = data_context
        self.__is_edit_view = is_edit_view
        self.__cur_participant = participant
        self.__on_data_updated = on_data_updated
        self.__lst_people = data_context.get_people()
        self.__lst_roles = data_context.get_roles()
        self.__service_id = data_context.get_curr_service().get_service_id()

        # set fields
        if is_edit_view:  # then set to the participant values passed in
            self.__person_id = participant.get_person_id()
            self.__person_name = participant.get_person_name()
            self.__role_id = participant.get_role_id()
            self.__role_name = participant.get_role_name()
        else:  # then set to default view
            self.__person_id = ''
            self.__role_id = ''
            self.__person_name = ''
            self.__role_name = ''

        # set up window
        self.__main_window = tkinter.Toplevel()
        self.__main_window.title(f"{'Edit' if is_edit_view else 'New'} Participant")
        self.__main_window.geometry('250x150')

        # set up frames
        self.__person_frame = tkinter.Frame(self.__main_window)
        self.__role_frame = tkinter.Frame(self.__main_window)
        self.__btn_frame = tkinter.Frame(self.__main_window)

        # set up person frame
        self.__selected_person_var = tkinter.StringVar()
        self.__person_lbl = tkinter.Label(self.__person_frame, text="Person")
        self.__person_option_menu = tkinter.OptionMenu(self.__person_frame, self.__selected_person_var,
                                                       *self.__lst_people, command=self.__set_selected_person)

        # set up role frame
        self.__selected_role_var = tkinter.StringVar()
        self.__role_lbl = tkinter.Label(self.__role_frame, text="Role")
        self.__role_option_menu = tkinter.OptionMenu(self.__role_frame, self.__selected_role_var,
                                                     *self.__lst_roles, command=self.__set_selected_role)

        # set up bottom btns
        self.__save_btn = tkinter.Button(self.__btn_frame, text="Save", command=self.__save)
        self.__cancel_btn = tkinter.Button(self.__btn_frame, text="Cancel", command=self.__main_window.destroy)

        # pack the elements
        self.__person_lbl.pack(side="left")
        self.__person_option_menu.pack(side="left", fill="x", expand=True)
        self.__role_lbl.pack(side="left")
        self.__role_option_menu.pack(side="left", fill="x", expand=True)
        self.__save_btn.pack(side="left")
        self.__cancel_btn.pack(side="left")
        self.__person_frame.pack(padx=10, pady=10, fill="x", expand=True)
        self.__role_frame.pack(padx=10, pady=10, fill="x", expand=True)
        self.__btn_frame.pack(padx=10, pady=10, anchor="e")

        # if is in edit mode, then set the value of the option menus and disable the person option menu
        if is_edit_view:
            self.__selected_person_var.set(self.__person_name)
            self.__selected_role_var.set(self.__role_name)
            self.__person_option_menu.config(state=tkinter.DISABLED)

        self.__main_window.mainloop()

    def __save(self):
        # validate the inputs
        if self.__person_id != '' and self.__role_id != '':  # then the inputs are valid
            if self.__is_edit_view == True:  # then in edit mode and need to update participant
                self.__cur_participant.set_person_id(self.__person_id)
                self.__cur_participant.set_role_id(self.__role_id)
                self.__cur_participant.set_person_name(self.__person_name)
                self.__cur_participant.set_role_name(self.__role_name)
                # update and display a message if the operation failed
                if not self.__data_context.update_participant(self.__cur_participant):
                    self.__display_error()
            else:  # then in create mode so need to add a new participant
                # create an empty participant for the user to fill out with a random id
                self.__cur_participant = Participant(self.__service_id, self.__person_name, self.__person_id,
                                                     self.__role_name, self.__role_id)
                # create and display a message if the operation failed
                if not self.__data_context.create_participant(self.__cur_participant):
                    self.__display_error()
            self.__on_data_updated()  # call the callback for the previous screen to update its data
            self.__main_window.destroy()
        else:  # then the inputs weren't valid
            tkinter.messagebox.showinfo("Error", "All fields must be filled out to continue")

    def __set_selected_person(self, person):
        self.__person_id = person.get_person_id()
        self.__person_name = str(person)  # returns the name of the person

    def __set_selected_role(self, role):
        self.__role_id = role.get_role_id()
        self.__role_name = role.get_role_name()

    def __display_error(self):
        tkinter.messagebox.showinfo("Error", "There was an error. Make sure that the person is not "
                                             "already assigned to a role for this service.")
