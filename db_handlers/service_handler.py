# Programmer: Andrew Dwyer
# Date: 4/26/22

import sqlite3
from data_models.service import Service


class ServiceHandler:
    def __init__(self, cur: sqlite3.Cursor):
        self.__cur = cur
        self.__create_table()

    def __create_table(self):
        try:
            self.__cur.execute('''CREATE TABLE IF NOT EXISTS Services (service_id INTEGER PRIMARY KEY NOT NULL, 
                                                                        start_datetime TEXT,
                                                                        service_name TEXT,
                                                                        description TEXT)''')
            return True
        except sqlite3.Error:
            return False

    def create_service(self, service):
        try:
            self.__cur.execute('''INSERT INTO Services
                                    (service_id, start_datetime, service_name, description)
                                    VALUES (?, ?, ?, ?)''',
                                (service.get_service_id(), service.get_start_datetime(),
                                 service.get_service_name(), service.get_description()))
            return True
        except sqlite3.Error:
            return False

    def get_services(self):
        try:
            self.__cur.execute('''SELECT * FROM Services''')
            res = self.__cur.fetchall()

            lst_services = []
            for service in res:
                lst_services.append(Service(service[0], service[1], service[2], service[3]))
            return lst_services
        except sqlite3.Error:
            return False

    def update_service(self, service):
        try:
            self.__cur.execute('''UPDATE Services SET
                                    start_datetime = ?,
                                    service_name = ?,
                                    description = ?
                                    WHERE service_id = ?''',
                                (service.get_start_datetime(), service.get_service_name(),
                                    service.get_description(), service.get_service_id()))
            return True
        except sqlite3.Error:
            return False

    def delete_service(self, service_id):
        try:
            self.__cur.execute('''DELETE FROM Services WHERE service_id = ?''', (service_id,))
            return True
        except sqlite3.Error:
            return False
