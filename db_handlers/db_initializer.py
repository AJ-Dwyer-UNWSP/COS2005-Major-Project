# Programmer: Andrew Dwyer
# Date: 4/26/22

import sqlite3


# this class sets up the connection to the db and handles the closing of that connection
class DBInitializer:
    def __init__(self):
        # connect to the db
        try:
            self.__conn = sqlite3.connect("./data.db")
            self.__cur = self.__conn.cursor()
            self.__cur.execute('PRAGMA foreign_keys=ON')  # turn on foreign key support
        except sqlite3.Error:
            print("There was an error connecting to the db")

    # closes the connection to the db
    def close(self):
        print("app closed")
        if self.__conn is not None:
            self.__conn.commit()
            self.__conn.close()

    # returns the reference to the db cursor
    def get_cur(self):
        return self.__cur
