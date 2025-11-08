import sqlite3
try:
    connection = sqlite3.connect("nisha_db.db")
    cursor = connection.cursor()
    insert_data_query = """
        INSERT INTO student(name,email,course,cgpa) VALUES (?,?,?,?)
        """
    student_records = [
        ("Nisha","amalinisha16@gmail.com","AIDS",8.9),
        ("Sania","saniasekar15@gamil.com","CSE",6.5),
        ("Jairesh","jairesh07@gamil.com","CSE",9.02)
    ]
    cursor.executemany(insert_data_query, student_records)
    connection.commit()
    print("All student records inserted successfully.")
except sqlite3.Error as error:
    print(error)
finally:
    cursor.close()
    connection.close()