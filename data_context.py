# Programmer: Andrew Dwyer
# Date: 4/27/22

from data_models.person import Person
import db_handlers.service_handler as service_handler
import db_handlers.role_handler as role_handler
import db_handlers.person_handler as person_handler
import db_handlers.participant_handler as participant_handler
from db_handlers.db_initializer import DBInitializer


class DataContext:
    def __init__(self, db_initializer: DBInitializer):
        # set up db handlers
        self.__db_init = db_initializer
        self.__service_handler = service_handler.ServiceHandler(self.__db_init.get_cur())
        self.__role_handler = role_handler.RoleHandler(self.__db_init.get_cur())
        self.__person_handler = person_handler.PersonHandler(self.__db_init.get_cur())
        self.__participant_handler = participant_handler.ParticipantHandler(self.__db_init.get_cur())

        # set up data fields
        self.__services = self.__service_handler.get_services()
        self.__curr_service = self.__services[0] if len(self.__services) > 0 else None
        self.__roles = self.__role_handler.get_roles()
        self.__people = self.__person_handler.get_people()
        self.__participants = self.__participant_handler.get_participants()

    # SERVICES
    # returns the list of services
    def get_services(self):
        return self.__services

    # gets the current service
    def get_curr_service(self):
        pass

    # sets the list of services
    def set_services(self, services):
        self.__services = services

    # sets the current service
    def set_curr_service(self, service):
        self.__curr_service = service

    # ROLES
    def get_roles(self):
        return self.__roles

    # PARTICIPANTS
    def get_participants(self):
        return self.__participants

    # PEOPLE
    def get_people(self):
        return self.__people

    # Deletes a person. Returns True if successful otherwise False.
    def delete_person(self, person):
        # remove the person from the db
        res = self.__person_handler.delete_person(person.get_person_id())
        # check that the operation didn't fail
        if not res:
            return False
        # remove the person from the list of people
        self.__people.remove(person)
        return True
