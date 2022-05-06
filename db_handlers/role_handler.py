# Programmer: Andrew Dwyer
# Date: 4/26/22

import sqlite3
from data_models.role import Role


class RoleHandler:
    def __init__(self, cur: sqlite3.Cursor):
        self.__cur = cur
        self.__create_table()

    # creates the table if it doesn't already exist
    def __create_table(self):
        try:
            self.__cur.execute('''CREATE TABLE IF NOT EXISTS Roles (role_id INTEGER PRIMARY KEY NOT NULL, 
                                                                        role_name TEXT)''')
            return True
        except sqlite3.Error:
            return False

    # creates a new role; returns true or false depending on if the operation is successful
    def create_role(self, role):
        try:
            self.__cur.execute('''INSERT INTO Roles
                                    (role_id, role_name)
                                    VALUES (?, ?)''',
                                (role.get_role_id(), role.get_role_name()))
            return True
        except sqlite3.Error:
            return False

    # returns all the roles from the db or false if the operation failed
    def get_roles(self):
        try:
            self.__cur.execute('''SELECT * FROM Roles''')
            res = self.__cur.fetchall()

            lst_roles = []
            for role in res:
                # add the roles to a list
                lst_roles.append(Role(role[0], role[1]))
            return lst_roles
        except sqlite3.Error:
            return False

    # update the role to the db
    def update_role(self, role):
        try:
            self.__cur.execute('''UPDATE Roles SET
                                    role_name = ?
                                    WHERE role_id = ?''',
                                (role.get_role_name(), role.get_role_id()))
            return True
        except sqlite3.Error:
            return False

    # delete the role from the db
    def delete_role(self, role_id):
        try:
            self.__cur.execute('''DELETE FROM Roles WHERE role_id = ?''', (role_id,))
            return True
        except sqlite3.Error:
            return False
