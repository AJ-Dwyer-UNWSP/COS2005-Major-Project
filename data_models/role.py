# Programmer: Andrew Dwyer
# Date: 4/26/22

# this is the data model for the Roles
class Role:
    def __init__(self, role_id, role_name):
        self.__role_id = role_id
        self.__role_name = role_name

    # getters
    def get_role_id(self):
        return self.__role_id

    def get_role_name(self):
        return self.__role_name

    # setters
    def set_role_name(self, name):
        self.__role_name = name

    def __str__(self):
        return str(self.__role_name)
