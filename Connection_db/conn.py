import sqlite3

conn = sqlite3.connect("connection_db/data.db")
cursor = conn.cursor()

cursor.execute("""create table if not exists Users (
                    Id integer primary key autoincrement, 
                    Nome string not null, 
                    Idade integer not null
               )
               """)

response = cursor.execute("select * from users").fetchall()

for i, value in enumerate(response):
    print(value[0])

conn.commit()
conn.close()