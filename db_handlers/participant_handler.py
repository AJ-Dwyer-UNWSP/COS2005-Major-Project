# Programmer: Andrew Dwyer
# Date: 4/26/22

import sqlite3
from data_models.participant import Participant


class ParticipantHandler:
    def __init__(self, cur: sqlite3.Cursor):
        self.__cur = cur
        self.__cur.execute('PRAGMA foreign_keys=ON')
        self.__create_table()

    def __create_table(self):
        self.__cur.execute('''CREATE TABLE IF NOT EXISTS Participants (person_id INTEGER NOT NULL, 
                                                                    service_id INTEGER NOT NULL,
                                                                    role_id INTEGER,
                                                                    PRIMARY KEY (person_id, service_id),
                                                                    FOREIGN KEY (person_id) REFERENCES People(person_id),
                                                                    FOREIGN KEY (service_id) REFERENCES Services(service_id),
                                                                    FOREIGN KEY(role_id) REFERENCES Roles(role_id))''')

    def create_participant(self, participant):
        self.__cur.execute('''INSERT INTO Participants
                                (person_id, service_id, role_id)
                                VALUES (?, ?, ?)''',
                           (participant.get_person_id(), participant.get_service_id(),
                            participant.get_role_id()))

    def get_participants(self):
        self.__cur.execute('''SELECT * FROM Participants''')
        res = self.__cur.fetchall()

        lst_participants = []
        for participant in res:
            lst_participants.append(Participant(participant[0], participant[1], participant[2]))
            print(Participant(participant[0], participant[1], participant[2]))
        return lst_participants

    def update_participant(self, participant):
        self.__cur.execute('''UPDATE Participants SET
                                role_id = ?
                                WHERE person_id = ? AND service_id = ?''',
                            (participant.get_role_id(), participant.get_person_id(),
                                participant.get_service_id()))

    def delete_participant(self, person_id, service_id):
        self.__cur.execute('''DELETE FROM Participants WHERE person_id = ? AND service_id = ?''', (person_id, service_id))
