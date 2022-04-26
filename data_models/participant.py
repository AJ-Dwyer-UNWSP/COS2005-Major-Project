# Programmer: Andrew Dwyer
# Date: 4/26/22

# this is the data model for the Participants
class Participant:
    def __init__(self, service_id, person_id, role_id):
        self.__service_id = service_id
        self.__person_id = person_id
        self.__role_id = role_id

    # getters
    def get_service_id(self):
        return self.__service_id

    def get_person_id(self):
        return self.__person_id

    def get_role_id(self):
        return self.__role_id

    # setters
    def set_service_id(self, service_id):
        self.__service_id = service_id

    def set_person_id(self, person_id):
        self.__person_id = person_id

    def set_role_id(self, role_id):
        self.__role_id = role_id

