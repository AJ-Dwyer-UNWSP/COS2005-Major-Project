# Programmer: Andrew Dwyer
# Date: 4/26/22

import sqlite3
from data_models.role import Role


class RoleHandler:
    def __init__(self, cur: sqlite3.Cursor):
        self.__cur = cur
        self.__create_table()

    def __create_table(self):
        self.__cur.execute('''CREATE TABLE IF NOT EXISTS Roles (role_id INTEGER PRIMARY KEY NOT NULL, 
                                                                    role_name TEXT)''')

    def create_role(self, role):
        self.__cur.execute('''INSERT INTO Roles
                                (role_id, role_name)
                                VALUES (?, ?)''',
                            (role.get_role_id(), role.get_role_name()))

    def get_roles(self):
        self.__cur.execute('''SELECT * FROM Roles''')
        res = self.__cur.fetchall()

        lst_roles = []
        for role in res:
            lst_roles.append(Role(role[0], role[1]))
        return lst_roles

    def update_role(self, role):
        self.__cur.execute('''UPDATE Roles SET
                                role_name = ?
                                WHERE role_id = ?''',
                            (role.get_role_name(), role.get_role_id()))

    def delete_role(self, role_id):
        self.__cur.execute('''DELETE FROM Roles WHERE role_id = ?''', (role_id,))
