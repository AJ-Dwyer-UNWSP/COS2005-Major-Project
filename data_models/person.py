# Programmer: Andrew Dwyer
# Date: 4/26/22

# this is the data model for the People
class Person:
    def __init__(self, person_id, first_name, last_name):
        self.__person_id = person_id
        self.__first_name = first_name
        self.__last_name = last_name

    # getters
    def get_person_id(self):
        return self.__person_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    # setters
    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

