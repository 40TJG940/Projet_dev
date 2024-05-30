import sqlite3


class SQLServer:

    def __init__(self):
        self.con = sqlite3.connect("game.db")
        self.cur = self.con.cursor()
    
    def create_table(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS game (id INTEGER PRIMARY KEY, name TEXT, score INTEGER)")
    
    def insert(self, name, score):
        self.cur.execute("INSERT INTO game (name, score) VALUES (?, ?)", (name, score))
        self.con.commit()
    
    def select(self):
        self.cur.execute("SELECT * FROM game")
        rows = self.cur.fetchall()
        return rows
    
    def close(self):
        self.con.close()