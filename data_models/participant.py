# Programmer: Andrew Dwyer
# Date: 4/26/22

# this is the data model for the Participants
# person_name is in the format 'last, first'
class Participant:
    def __init__(self, service_id, person_name, person_id, role_name, role_id):
        # set the data fields
        self.__service_id = service_id
        self.__person_name = person_name
        self.__person_id = person_id
        self.__role_name = role_name
        self.__role_id = role_id

    # getters
    def get_service_id(self):
        return self.__service_id

    def get_person_name(self):
        return self.__person_name

    def get_person_id(self):
        return self.__person_id

    def get_role_name(self):
        return self.__role_name

    def get_role_id(self):
        return self.__role_id

    # setters
    def set_service_id(self, service_id):
        self.__service_id = service_id

    def set_person_name(self, person_name):
        self.__person_name = person_name

    def set_person_id(self, person_id):
        self.__person_id = person_id

    def set_role_name(self, role_name):
        self.__role_name = role_name

    def set_role_id(self, role_id):
        self.__role_id = role_id

    def __str__(self):
        # in the format 'last name, first name – role name'
        return f'{self.get_person_name()} – {self.get_role_name()}'
