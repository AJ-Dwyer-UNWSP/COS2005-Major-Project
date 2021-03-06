# Programmer: Andrew Dwyer
# Date: 4/26/22

import sqlite3
from data_models.participant import Participant


# this class handles the db operations for the Participants table
class ParticipantHandler:
    def __init__(self, cur: sqlite3.Cursor):
        self.__cur = cur
        self.__create_table()

    # this function creates a table if it does not already exist; returns True is successful, otherwise False
    def __create_table(self):
        try:
            self.__cur.execute('''CREATE TABLE IF NOT EXISTS Participants 
                                                        (person_id INTEGER NOT NULL, 
                                                        service_id INTEGER NOT NULL,
                                                        role_id INTEGER,
                                                        PRIMARY KEY (person_id, service_id),
                                                        FOREIGN KEY (person_id) REFERENCES People(person_id) ON DELETE CASCADE,
                                                        FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE CASCADE,
                                                        FOREIGN KEY(role_id) REFERENCES Roles(role_id) ON DELETE CASCADE)''')
            return True
        except sqlite3.Error:
            return False

    # this function creates a participant
    def create_participant(self, participant):
        try:
            self.__cur.execute('''INSERT INTO Participants
                                    (person_id, service_id, role_id)
                                    VALUES (?, ?, ?)''',
                               (participant.get_person_id(), participant.get_service_id(),
                                participant.get_role_id()))
            return True
        except sqlite3.Error:
            return False

    # this function gets all participants for a service_id and returns the list of participants
    # if there was an error it returns False
    def get_participants(self, service_id):
        try:
            # this selects both the participant and the corresponding person name
            # and role_id from the People and Roles tables
            self.__cur.execute('''SELECT Participants.service_id, People.last_name, People.first_name, 
                                    Participants.person_id, Roles.role_name, Participants.role_id
                                    FROM Participants, Roles, People
                                    WHERE Participants.service_id = ? AND 
                                    Participants.role_id = Roles.role_id AND 
                                    Participants.person_id = People.person_id''', (service_id,))
            res = self.__cur.fetchall()

            lst_participants = []
            for participant in res:
                # Arguments: service_id, "last_name, first_name", person_id, roles_name, role_id
                lst_participants.append(Participant(participant[0], (f"{participant[1]}, {participant[2]} "),
                                                    participant[3], participant[4], participant[5]))
            return lst_participants
        except sqlite3.Error:
            return False

    # updates the role id of the participant
    def update_participant(self, participant):
        try:
            self.__cur.execute('''UPDATE Participants SET
                                    role_id = ?
                                    WHERE person_id = ? AND service_id = ?''',
                                (participant.get_role_id(), participant.get_person_id(),
                                    participant.get_service_id()))
            return True
        except sqlite3.Error:
            return False

    # deletes a participant with the corresponding person_id and service_id
    def delete_participant(self, person_id, service_id):
        try:
            self.__cur.execute('''DELETE FROM Participants WHERE person_id = ? AND service_id = ?''',
                               (person_id, service_id))
            return True
        except sqlite3.Error:
            return False
