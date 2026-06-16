import sqlite3

conn = sqlite3.connect("connection_db/data.db")
cursor = conn.cursor()

cursor.execute("""create table if not exists Users (
                    Id integer primary key autoincrement, 
                    Nome string not null, 
                    Idade integer not null
               )
               """)
#cursor.execute("INSERT INTO users (Nome, Idade) VALUES ('Lucas', 21)")

#cursor.execute("DELETE FROM users WHERE Id == 2")

cursor.execute("UPDATE users SET Nome = 'João' WHERE Id = 3")

response = cursor.execute("select * from users").fetchall()

for value in response:
    print(value)

conn.commit()
conn.close()