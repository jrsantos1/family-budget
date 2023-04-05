import sqlite3

class conection_sqllite_3:

    con = sqlite3.connect('family_budget.db')

    @classmethod
    def get_connection(cls):
        return cls.con

    @classmethod
    def get_connection_cursor(self):
        return self.con.cursor()