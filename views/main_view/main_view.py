# Programmer: Andrew Dwyer
# Date: 4/26/22

import tkinter
from views.people.list_people import ListPeopleView
from views.roles.list_roles import ListRolesView
from views.services.new_edit_service import NewEditServiceView
from views.participants.new_edit_participant import NewEditParticipantView
from data_context import DataContext
import tkinter.messagebox


# this is the main view of the application
class MainView:
    def __init__(self, data_context: DataContext):
        # create a data context
        self.__data_context = data_context
        self.__lst_services = self.__data_context.get_services()
        if len(self.__lst_services) > 0:
            self.__curr_service = self.__lst_services[0]
            self.__data_context.set_curr_service(self.__curr_service)
            self.__lst_participants = self.__data_context.get_participants()
            self.__curr_participant = self.__lst_participants[0] if len(self.__lst_participants) > 0 else None
        else:
            self.__curr_service = None
            self.__lst_participants = []
            self.__curr_participant = None

        # set the window up
        self.__main_window = tkinter.Tk()
        self.__main_window.title("Streamlined Service")
        self.__main_window.minsize(600, 300)  # set the minsize the window

        # set up frames
        self.__menu_frame = tkinter.Frame(self.__main_window)  # this is the top frame for the menu buttons
        self.__main_frame = tkinter.Frame(self.__main_window)  # this is the main frame for the content
        self.__list_services_frame = tkinter.Frame(self.__main_frame)
        self.__service_content_frame = tkinter.Frame(self.__main_frame, highlightbackground="black",
                                                     highlightthickness=1)

        # set up and pack menu buttons
        self.__setup_menu_btns()

        # setup and pack the listbox()
        self.__setup_list_box()

        self.__setup_service_content()

        # pack the frames
        self.__menu_frame.pack()
        self.__main_frame.pack(fill="both", pady=10, padx=10, expand=True)
        self.__list_services_frame.pack(side="left", anchor='w', fill="y", expand=False, padx=5)
        self.__service_content_frame.pack(side="left", fill="both", expand=True, padx=5)

        # set the listbox to select the first service
        self.__list_services_box.select_set(0)  # This only sets focus on the first item.
        self.__list_services_box.event_generate("<<ListboxSelect>>")

        # start the mainloop
        self.__main_window.mainloop()

    def __setup_menu_btns(self):
        self.__new_service_btn = tkinter.Button(self.__menu_frame, text="New Service", command=self.__new_service)
        self.__delete_service_btn = tkinter.Button(self.__menu_frame, text="Delete Service", command=self.__delete_service)
        self.__edit_service_btn = tkinter.Button(self.__menu_frame, text="Edit Service", command=self.__edit_service)
        self.__view_roles_btn = tkinter.Button(self.__menu_frame, text="View Roles", command=self.__view_roles)
        self.__view_people_btn = tkinter.Button(self.__menu_frame, text="View People", command=self.__view_people)
        self.__quit_btn = tkinter.Button(self.__menu_frame, text="Quit", command=self.__main_window.destroy)

        # pack the buttons
        self.__new_service_btn.pack(side="left")
        self.__delete_service_btn.pack(side="left")
        self.__edit_service_btn.pack(side="left")
        self.__view_roles_btn.pack(side="left")
        self.__view_people_btn.pack(side="left")
        self.__quit_btn.pack(side="left")

    def __setup_list_box(self):
        self.__list_services_var = tkinter.StringVar()
        self.__list_services_var.set(self.__lst_services)
        self.__list_services_box = tkinter.Listbox(self.__list_services_frame, listvariable=self.__list_services_var)
        # bind to the event that an item is clicked in the listbox
        self.__list_services_box.bind("<<ListboxSelect>>", self.__on_listbox_item_click)
        # create the scrollbar
        self.__scroll_bar = tkinter.Scrollbar(self.__list_services_frame, orient=tkinter.VERTICAL,
                                              command=self.__list_services_box.yview)
        # set the listbox to set the scroll bar when it moves
        self.__list_services_box.config(yscrollcommand=self.__scroll_bar.set)

        # pack the elements
        self.__list_services_box.pack(side="left", fill="y")
        self.__scroll_bar.pack(side="right", fill=tkinter.Y)

    def __setup_service_content(self):
        # set default text if the values are None
        self.__serv_title_var = tkinter.StringVar()
        self.__serv_desc_var = tkinter.StringVar()
        if self.__curr_service is not None:
            self.__serv_title_var.set(str(self.__curr_service))
            self.__serv_desc_var.set(self.__curr_service.get_description())
        self.__service_title = tkinter.Label(self.__service_content_frame, textvariable=self.__serv_title_var, font=("TkDefaultFont", 18))
        self.__service_desc = tkinter.Label(self.__service_content_frame, textvariable=self.__serv_desc_var)

        # participants listbox
        self.__prtcpts_frame = tkinter.Frame(self.__service_content_frame)
        self.__list_prtcpts_var = tkinter.StringVar()
        self.__list_prtcpts_var.set(self.__lst_participants)
        self.__list_prtcpt_box = tkinter.Listbox(self.__prtcpts_frame, listvariable=self.__list_prtcpts_var)
        # bind to the event that an item is clicked in the listbox
        self.__list_prtcpt_box.bind("<<ListboxSelect>>", self.__on_prtcpts_listbox_item_click)
        # create the scrollbar
        self.__prtcpt_scroll_bar = tkinter.Scrollbar(self.__prtcpts_frame, orient=tkinter.VERTICAL,
                                                     command=self.__list_prtcpt_box.yview)
        # set the listbox to set the scroll bar when it moves
        self.__list_prtcpt_box.config(yscrollcommand=self.__prtcpt_scroll_bar.set)

        # participant buttons
        self.__prtcpt_btn_frame = tkinter.Frame(self.__service_content_frame)
        self.__add_prtcpt_btn = tkinter.Button(self.__prtcpt_btn_frame, text="Add Participant", command=self.__add_participant)
        self.__edit_prtcpt_btn = tkinter.Button(self.__prtcpt_btn_frame, text="Edit Participant", command=self.__edit_participant)
        self.__delete_prtcpt_btn = tkinter.Button(self.__prtcpt_btn_frame, text="Remove Participant", command=self.__delete_participant)

        # pack the elements
        self.__service_title.pack(side="top", anchor="nw", padx=5, pady=3)
        self.__service_desc.pack(anchor="w", padx=5)
        self.__prtcpts_frame.pack(expand=True, fill="both", padx=10, pady=6)
        self.__list_prtcpt_box.pack(side="left", fill="both", expand=True)
        self.__prtcpt_scroll_bar.pack(side="right", fill=tkinter.Y)
        self.__prtcpt_btn_frame.pack(pady=5, padx=5)
        self.__add_prtcpt_btn.pack(side="left")
        self.__edit_prtcpt_btn.pack(side="left")
        self.__delete_prtcpt_btn.pack(side="left")

    def __on_listbox_item_click(self, event):
        try:
            index = self.__list_services_box.curselection()
            # if the lenght of index is 0 than it means the user is editing on another screen
            # and the curr service shouldn't change
            if len(index) != 0:
                self.__curr_service = self.__lst_services[index[0]]
                self.__data_context.set_curr_service(self.__curr_service)
        except IndexError as err:  # catch any possible errors
            print(err)
            self.__curr_service = self.__lst_services[0]
            self.__data_context.set_curr_service(self.__curr_service)
        finally:  # set the participants and update the UI
            self.__lst_participants = self.__data_context.get_participants()
            self.__curr_participant = self.__lst_participants[0] if len(self.__lst_participants) > 0 else None
            self.__update_UI()

    def __on_prtcpts_listbox_item_click(self, event):
        index = self.__list_prtcpt_box.curselection()[0]
        self.__curr_participant = self.__lst_participants[index]

    def __new_service(self):
        NewEditServiceView(self.__data_context, False, None, self.__on_update)

    def __edit_service(self):
        # open the edit view if the current person is not None to avoid an Exception
        if self.__curr_service is not None:
            NewEditServiceView(self.__data_context, True, self.__curr_service, self.__on_update)
        else:
            tkinter.messagebox.showinfo("Error", "Please select an item before performing your operation.")

    def __delete_service(self):
        if not self.__data_context.delete_service(self.__curr_service):
            self.__display_error()
        else:
            self.__on_update()

    def __view_roles(self):
        ListRolesView(self.__data_context, self.__on_update)

    def __view_people(self):
        ListPeopleView(self.__data_context, self.__on_update)

    def __add_participant(self):
        NewEditParticipantView(self.__data_context, False, None, self.__on_update)

    def __edit_participant(self):
        NewEditParticipantView(self.__data_context, True, self.__curr_participant, self.__on_update)

    def __delete_participant(self):
        if self.__curr_participant:
            if not self.__data_context.delete_participant(self.__curr_participant):
                self.__display_error()
            else:
                self.__on_update()

    def __display_error(self):
        tkinter.messagebox.showinfo("Error", "There was an error. Please try again.")

    def __on_update(self):
        # update the data
        self.__lst_services = self.__data_context.get_services()
        if len(self.__lst_services) > 0:
            self.__curr_service = self.__data_context.get_curr_service()
            self.__data_context.set_curr_service(self.__curr_service)
            self.__lst_participants = self.__data_context.get_participants()
            self.__curr_participant = self.__lst_participants[0] if len(self.__lst_participants) > 0 else None
        else:
            self.__curr_service = None
            self.__lst_participants = []
            self.__curr_participant = None
        self.__update_UI()

    def __update_UI(self):
        self.__list_services_var.set(self.__lst_services)
        self.__list_prtcpts_var.set(self.__lst_participants)
        self.__serv_title_var.set(self.__curr_service.get_service_name())
        self.__serv_desc_var.set(self.__curr_service.get_description())
