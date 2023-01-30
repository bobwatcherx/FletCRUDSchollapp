import sqlite3
conn = sqlite3.connect("db/dbone.db",check_same_thread=False)


# THIS SCRIPT IS CREATE TABEL AUTOMATICALLY WHEN YOU RUN THE FLET APP

def create_table():
	c = conn.cursor()
	c.execute("""CREATE TABLE IF NOT EXISTS users(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT,
		contact TEXT,
		age INTEGER,
		gender TEXT,
		email TEXT,
		address TEXT)
		""")
	conn.commit()
