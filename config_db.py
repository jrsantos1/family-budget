import sqlite3

class conection_sqllite_3:

    con = sqlite3.connect('family_budget.db', check_same_thread=False)

    @classmethod
    def get_connection(cls):
        return cls.con

    @classmethod
    def get_connection_cursor(self) -> con.cursor():
        return self.con.cursor()