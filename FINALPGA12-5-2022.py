#Q1. Create a class call Student with following functions inside the class.
#a) Create __init__() that asks user for student name, and name of the school.
#b) Create a function call get_grade() that checks entered grade. The grade must be K through 5
#c) Create a function call print_student that prints information about student including Name,
#School and Grade
#d) Instantiate an object call student_info to access information.
#=====================================================================================
#Your output should look like below
#What is the name of student? Mickey
#What is the name of school? Disney
#What is student's grade? [K, 1-5]3
#Name: Mickey
#School: Disney
#Grade: 3
#=====================
class STUDENT:

    def __init__(SELF, STUDENTNAME, SCHOOLN, GRADE):
        SELF.STUDENTNAME = STUDENTNAME
        SELF.SCHOOLN = SCHOOLN
        SELF.GRADE = GRADE
    def input(SELF):
        A  = input("What is the name of the student")
        B = input("What is the name of the school?")
        SELF.STUDENTNAME = A
        SELF.SCHOOLN = B
    def GET_GRADE(SELF):
        C = int(input("What is the student's grade?"))
        SELF.GRADE = C
        if SELF.GRADE >= 5:
            print("This is not a valid grade input:")
        else:
            print("The grade is:", SELF.GRADE)      
    def PRINT_STUDENT(SELF):
        print("Name",SELF.STUDENTNAME)
        print("School:", SELF.SCHOOLN)
        print("GRADE:", SELF.GRADE)

student_info = STUDENT( " ", " ", " ")
student_info.input()
student_info.GET_GRADE()
student_info.PRINT_STUDENT()
