# Programmer: Andrew Dwyer
# Date: 4/27/22

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
        # make sure that there are services before setting the current service and participants
        if len(self.__services) > 0:
            self.__curr_service = self.__services[0]
            self.__participants = self.__participant_handler.get_participants(self.__curr_service.get_service_id())
        else:
            self.__curr_service = None
            self.__participants = []
        self.__roles = self.__role_handler.get_roles()
        self.__people = self.__person_handler.get_people()

    # SERVICES
    # returns the list of services
    def get_services(self):
        return self.__services

    # gets the current service
    def get_curr_service(self):
        return self.__curr_service

    # sets the list of services
    def set_services(self, services):
        self.__services = services

    # sets the current service
    def set_curr_service(self, service):
        self.__curr_service = service
        self.__participants = self.__participant_handler.get_participants(self.__curr_service.get_service_id())

    # Deletes a service. Returns True if successful otherwise False.
    def delete_service(self, service):
        # remove the service from the db
        res = self.__service_handler.delete_service(service.get_service_id())
        # check that the operation didn't fail
        if not res:
            return False
        # remove the service from the list of services
        self.__services.remove(service)
        self.set_curr_service(self.__services[0])
        return True

    def create_service(self, service):
        # add the service to the db
        res = self.__service_handler.create_service(service)
        # check that the operation didn't fail
        if not res:
            return False
        # add the service to the list of services
        self.__services.append(service)
        return True

    def update_service(self, service):
        # add the service to the db
        res = self.__service_handler.update_service(service)
        # check that the operation didn't fail
        if not res:
            return False
        # update the list with the updated service at the old index
        self.__services[self.__services.index(service)] = service
        return True

    # ROLES
    def get_roles(self):
        return self.__roles

    # Deletes a role. Returns True if successful otherwise False.
    def delete_role(self, role):
        # remove the role from the db
        res = self.__role_handler.delete_role(role.get_role_id())
        # check that the operation didn't fail
        if not res:
            return False
        # remove the role from the list of roles
        self.__roles.remove(role)
        return True

    def create_role(self, role):
        # add the role to the db
        res = self.__role_handler.create_role(role)
        # check that the operation didn't fail
        if not res:
            return False
        # add the role to the list of roles
        self.__roles.append(role)
        return True

    def update_role(self, role):
        # add the role to the db
        res = self.__role_handler.update_role(role)
        # check that the operation didn't fail
        if not res:
            return False
        # update the list with the updated role at the old index
        self.__roles[self.__roles.index(role)] = role
        return True

    # PARTICIPANTS
    def get_participants(self):
        return self.__participants

    # Deletes a participant. Returns True if successful otherwise False.
    def delete_participant(self, participant):
        # remove the participant from the db
        res = self.__participant_handler.delete_participant(participant.get_person_id(), participant.get_service_id())
        # check that the operation didn't fail
        if not res:
            return False
        # remove the participant from the list of participants
        self.__participants.remove(participant)
        # remove all the participants for the participant
        return True

    def create_participant(self, participant):
        # add the participant to the db
        res = self.__participant_handler.create_participant(participant)
        # check that the operation didn't fail
        if not res:
            return False
        # add the participant to the list of participants
        self.__participants.append(participant)
        return True

    def update_participant(self, participant):
        # add the participant to the db
        res = self.__participant_handler.update_participant(participant)
        # check that the operation didn't fail
        if not res:
            return False
        # update the list with the updated participant at the old index
        self.__participants[self.__participants.index(participant)] = participant
        return True

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

    def create_person(self, person):
        # add the person to the db
        res = self.__person_handler.create_person(person)
        # check that the operation didn't fail
        if not res:
            return False
        # add the person to the list of people
        self.__people.append(person)
        return True

    def update_person(self, person):
        # add the person to the db
        res = self.__person_handler.update_person(person)
        # check that the operation didn't fail
        if not res:
            return False
        # update the list with the updated person at the old index
        self.__people[self.__people.index(person)] = person
        return True
