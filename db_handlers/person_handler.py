# Programmer: Andrew Dwyer
# Date: 4/26/22

import sqlite3
from data_models.person import Person


# this class handles the db operations for the People table
class PersonHandler:
    def __init__(self, cur: sqlite3.Cursor):
        self.__cur = cur
        self.__create_table()

    # create a table if it doesn't already exist; returns True id successful otherwise False if there was an error
    def __create_table(self):
        try:
            self.__cur.execute('''CREATE TABLE IF NOT EXISTS People (person_id INTEGER PRIMARY KEY NOT NULL, 
                                                                        first_name TEXT,
                                                                        last_name TEXT)''')
            return True
        except sqlite3.Error:
            return False

    # create a new person in the db
    # returns True if successful otherwise False
    def create_person(self, person):
        try:
            self.__cur.execute('''INSERT INTO People
                                    (person_id, first_name, last_name)
                                    VALUES (?, ?, ?)''',
                               (person.get_person_id(), person.get_first_name(),
                                person.get_last_name()))
            return True
        except sqlite3.Error:
            return False

    # gets all people from the db; returns the list of people if successful and false if there was an error
    def get_people(self):
        try:
            self.__cur.execute('''SELECT * FROM People''')
            res = self.__cur.fetchall()

            lst_people = []
            for person in res:
                lst_people.append(Person(person[0], person[1], person[2]))
            return lst_people
        except sqlite3.Error:
            return False

    # updates the person to the db
    def update_person(self, person):
        try:
            self.__cur.execute('''UPDATE People SET
                                    first_name = ?,
                                    last_name = ?
                                    WHERE person_id = ?''',
                                (person.get_first_name(), person.get_last_name(),
                                    person.get_person_id()))
            return True
        except sqlite3.Error:
            return False

    # deletes the person from the db
    def delete_person(self, person_id):
        try:
            self.__cur.execute('''DELETE FROM People WHERE person_id = ?''', (person_id,))
            return True
        except sqlite3.Error:
            return False
