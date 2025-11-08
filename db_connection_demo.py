import sqlite3
try:
    # Connection to the database
    connection = sqlite3.connect('nisha_db.db')
    cursor = connection.cursor()
    # Select and print data
    cursor.execute("SELECT * FROM book")
    print("Students in the database:")
    for row in cursor.fetchall():
        print(row)
except sqlite3.Error as e:
    print(f"SQlite Error:{e}")
finally:
    if connection:
        connection.close()