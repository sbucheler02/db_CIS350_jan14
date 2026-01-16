import sqlite3

conn = sqlite3.connect('points.db')
cursor = conn.cursor()
query = """
    DELETE FROM points WHERE id > 3;
"""

cursor.execute(query)
conn.commit()
conn.close()