import sqlite3

conn = sqlite3.connect('del.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS person2 (
 answer_id INTEGER PRIMARY KEY AUTOINCREMENT,
 first_name text NOT NULL,
 last_name text NOT NULL
);""")

# c.execute("""CREATE TABLE IF NOT EXISTS answer (
# answer_id INTEGER AUTOINCREMENT PRIMARY KEY,
# question text NOT NULL,
# answer text NOT NULL
# );""")


conn.commit()
c.close()
conn.close()