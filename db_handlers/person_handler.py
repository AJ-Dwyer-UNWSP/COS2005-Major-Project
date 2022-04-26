# Programmer: Andrew Dwyer
# Date: 4/26/22

import sqlite3
from data_models.person import Person


class PersonHandler:
    def __init__(self, cur: sqlite3.Cursor):
        self.__cur = cur
        self.__create_table()

    def __create_table(self):
        self.__cur.execute('''CREATE TABLE IF NOT EXISTS People (person_id INTEGER PRIMARY KEY NOT NULL, 
                                                                    first_name TEXT,
                                                                    last_name TEXT)''')

    def create_person(self, person):
        self.__cur.execute('''INSERT INTO People
                                (person_id, first_name, last_name)
                                VALUES (?, ?, ?)''',
                           (person.get_person_id(), person.get_first_name(),
                            person.get_last_name()))

    def get_people(self):
        self.__cur.execute('''SELECT * FROM People''')
        res = self.__cur.fetchall()

        lst_people = []
        for person in res:
            lst_people.append(Person(person[0], person[1], person[2]))
        return lst_people

    def update_person(self, person):
        self.__cur.execute('''UPDATE People SET
                                first_name = ?,
                                last_name = ?
                                WHERE person_id = ?''',
                            (person.get_first_name(), person.get_last_name(),
                                person.get_person_id()))

    def delete_person(self, person_id):
        self.__cur.execute('''DELETE FROM People WHERE person_id = ?''', (person_id,))
