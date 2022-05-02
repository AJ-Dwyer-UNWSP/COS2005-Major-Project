# Programmer: Andrew Dwyer
# Date: 4/26/22

# this is the data model for the Services
class Service:
    def __init__(self, service_id, start_datetime, service_name, description):
        self.__service_id = service_id
        self.__start_datetime = start_datetime
        self.__service_name = service_name
        self.__description = description

    # getters
    def get_service_id(self):
        return self.__service_id

    def get_service_name(self):
        return self.__service_name

    def get_start_datetime(self):
        return self.__start_datetime

    def get_description(self):
        return self.__description

    # setters
    def set_service_name(self, name):
        self.__service_name = name

    def set_start_datetime(self, start_datetime):
        self.__start_datetime = start_datetime

    def set_description(self, description):
        self.__description = description

    def __str__(self):
        return str(f"{self.get_service_name()} – {self.get_start_datetime()}")
