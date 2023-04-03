import sqlite3

class conection_sqllite_3:

    con = sqlite3.connect('family_budget.db')

    def get_connection(self):
        return self.con

    def get_connection_cursor(self):
        return self.con.cursor()