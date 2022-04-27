# Programmer: Andrew Dwyer
# Date: 4/26/22

import sqlite3


class DBInitializer:
    def __init__(self):
        try:
            self.__conn = sqlite3.connect("./data.db")
            self.__cur = self.__conn.cursor()
        except sqlite3.Error as err:
            print(err)
            print("There was an error connecting to the db")

    def close(self):
        print("close")
        if self.__conn is not None:
            self.__conn.commit()
            self.__conn.close()

    def get_cur(self):
        return self.__cur
