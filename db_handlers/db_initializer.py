# Programmer: Andrew Dwyer
# Date: 4/26/22

import sqlite3
import db_handlers.service_handler as service_handler
import db_handlers.role_handler as role_handler
import db_handlers.person_handler as person_handler
import db_handlers.participant_handler as participant_handler
from data_models.participant import Participant


class DBInitializer:
    def __init__(self):
        try:
            self.__conn = sqlite3.connect("./data.db")
            self.__cur = self.__conn.cursor()

            sh = service_handler.ServiceHandler(self.__cur)
            rh = role_handler.RoleHandler(self.__cur)
            ph = person_handler.PersonHandler(self.__cur)
            prh = participant_handler.ParticipantHandler(self.__cur)
            participant = Participant(2, 2, 2)
            prh.create_participant(participant)
            print(len(prh.get_participants()))
            participant.set_role_id(10)
            prh.update_participant(participant)
            print(len(prh.get_participants()))
            prh.delete_participant(participant.get_person_id(), participant.get_service_id())
            print(len(prh.get_participants()))
        except sqlite3.Error as err:
            print(err)
            print("There was an error connecting to the db")

    def close(self):
        if self.__conn is not None:
            self.__conn.commit()
            self.__conn.close()

    def get_cur(self):
        return self.__cur
