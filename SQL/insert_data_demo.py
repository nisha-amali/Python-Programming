import sqlite3
try:
    connection = sqlite3.connect("nisha_db.db")
    cursor = connection.cursor()
    insert_data_query = """
        INSERT INTO student(name,email,course,cgpa) VALUES (?,?,?,?)
        """
    student_data = ("Nisha","amalinisha16@gamil.com","AIDS","8.9")
    cursor.execute(insert_data_query, student_data)
    connection.commit()
    print("Data inserted successfully.")
except sqlite3.Error as error:
    print(error)
finally:
    cursor.close()
    connection.close()