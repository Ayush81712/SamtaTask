import mysql.connector

connection = mysql.connector.connect(
    host="localhost", 
    user="root",  
    password="root",  
    database="students" 
)

cursor = connection.cursor()

cursor.execute('select version()')
data = cursor.fetchone()
print(data)


create_table_query = """
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT,
    grade FLOAT
)
"""
cursor.execute(create_table_query)


insert_query = """
INSERT INTO students (first_name, last_name, age, grade)
VALUES (%s, %s, %s, %s)
"""
student_data = ("Alice", "Smith", 18, 95.5)
cursor.execute(insert_query, student_data)

connection.commit()

# # Update the grade of the student with the first name "Alice"
update_query = """
UPDATE students
SET grade = %s
WHERE first_name = %s
"""
new_grade = 97.0
cursor.execute(update_query, (new_grade, "Alice"))
connection.commit()

# # Delete the student with the last name "Smith"
delete_query = """
DELETE FROM students
WHERE last_name = %s
"""
student_last_name = "Smith"
cursor.execute(delete_query, (student_last_name,))
connection.commit()

# # Fetch and display all student records
select_query = "SELECT * FROM students"
cursor.execute(select_query)
students = cursor.fetchall()

for student in students:
    print(f"Student ID: {student[0]}, First Name: {student[1]}, Last Name: {student[2]}, Age: {student[3]}, Grade: {student[4]}")

# Close the cursor and the connection
cursor.close()
connection.close()
