import sys

# Make a txt file with a list of students with their respective grades
# Highest is 1.00 while lowest is 5.00
with open("C:/Users/Tou/Desktop/School/OOPPython Stuff/GWA/master_list.txt") as gwa_reader:
    students_stats = gwa_reader.readlines()
    top_student_name = ""
    top_student_grade = ""

    topmost_grade = 1.00

    # Separate the name from the grade in the text file
    for line in students_stats:
        student_name, student_grade = line.split("| ")
        student_grade = float(student_grade)
