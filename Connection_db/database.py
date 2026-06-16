import sqlite3

class DatabaseRepository:
    def __init__(self):
        self.conn = sqlite3.connect("connection_db/data.db")
        self.cursor = self.conn.cursor()
        
    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Users_app (
                Id integer primary key autoincrement,
                Nome string not null,
                Idade integer not null
            )""")
        self.conn.commit()
        
    def insert_complete_data(self, data):
        self.cursor.execute("""insert into Users_app (Nome, Idade) values (?, ?)""", data)
        self.conn.commit()
        
    def delete_data_by_id(self, user_id):
        self.cursor.execute("""DELETE FROM Users_app WHERE Id == ?""", user_id)
        self.conn.commit()
        
    def getAll_data(self, query):
        self.cursor.execute("""SELECT * FROM Users_app""")
        return self.cursor.fetchall()
    
    def getOne_data(self, user_id):
        self.cursor.execute("""SELECT * FROM Users_app WHERE Id == ?""", user_id)
        return self.cursor.fetchone()