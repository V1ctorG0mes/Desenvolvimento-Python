# requesting student data
student_email = input("Provide the student's email: ")
semester_grade = input("Provide the student's semester grade: ")

# converting the grade to float format
semester_grade = float(semester_grade)

# performing the logical test
if semester_grade > 8.5:
    print("SENDING EMAIL TO {}".format(student_email))