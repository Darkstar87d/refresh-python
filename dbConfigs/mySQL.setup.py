import sqlite3

# Create a connection to the database (creates it if it doesn't exist)
conn = sqlite3.connect('refreshSql.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    email TEXT
                )''')

# Commit the changes and close the connection
conn.commit()
conn.close()