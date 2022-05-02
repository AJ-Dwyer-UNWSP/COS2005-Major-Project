# Programmer: Andrew Dwyer
# Date: 4/26/22

import tkinter
from views.people.list_people import ListPeopleView
from data_context import DataContext


# this is the main view of the application
class MainView:
    def __init__(self, data_context: DataContext):
        # create a data context
        self.__data_context = data_context
        self.__lst_services = self.__data_context.get_services()
        if len(self.__lst_services) > 0:
            self.__curr_service = self.__lst_services[0]
            data_context.set_curr_service(self.__curr_service)
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
        if self.__curr_service is not None:
            serv_title = str(self.__curr_service)
            serv_desc = self.__curr_service.get_description()
        else:
            serv_title = ''
            serv_desc = ''
        self.__service_title = tkinter.Label(self.__service_content_frame, text=serv_title, font=("TkDefaultFont", 18))
        self.__service_desc = tkinter.Label(self.__service_content_frame, text=serv_desc)

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
        index = self.__list_services_box.curselection()[0]
        self.__curr_person = self.__lst_services[index]

    def __on_prtcpts_listbox_item_click(self, event):
        index = self.__list_prtcpt_box.curselection()[0]
        self.__curr_participant = self.__lst_participants[index]

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

    def __add_participant(self, event):
        pass

    def __edit_participant(self, event):
        pass

    def __delete_participant(self, event):
        pass
