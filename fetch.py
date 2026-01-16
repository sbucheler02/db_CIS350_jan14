import sqlite3

conn = sqlite3.connect('points.db')
cursor = conn.cursor()
query = """
    SELECT *
    FROM points;
"""

cursor.execute(query)
results = cursor.fetchall()
conn.close()

print(results)