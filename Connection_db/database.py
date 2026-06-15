import sqlite3

class DatabaseRepository:
    def __init__(self):
        self.conn = sqlite3.connect("connection_db/data.db")
        self.cursor = self.conn.cursor()
        
    def create_table(self, query):
        self.cursor.execute(query)
        self.conn.commit()
        self.conn.close()
        
    def insert_data(self, query, data):
        self.cursor.execute(query, data)
        self.conn.commit()
        self.conn.close()
        
    def getAll_data(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def getOne_data(self, query, data):
        self.cursor.execute(query, data)
        return self.cursor.fetchone()