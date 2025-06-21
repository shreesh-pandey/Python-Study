# Q.6: Write a Python program to calculate the grade of a student based on their marks and then display the corresponding grade.
    
#     The grading scheme is as follows:
#     | Marks (%)     | Grade |
#     |---------------|-------|
#     | 90 to 100     | Ex    |
#     | 80 to 89      | A     |
#     | 70 to 79      | B     |
#     | 60 to 69      | C     |
#     | 50 to 59      | D     |
#     | Below 50      | F     |

# Lets start with asking user to input the Student's name and their marks.
name = input("Please enter the name of the student: ")
marks = int(input(f"Please enter the overall marks {name} has obtained: "))

# Lets use dictionary to assign the grading scheme.
grading = {"Ex": marks >= 90,
           "A": 90 > marks >= 80,
           "B": 80 > marks >= 70,
           "C": 70 > marks >= 60,
           "D": 60 > marks >= 50,
           "F": marks < 50}

for grade, condition in grading.items():
    if condition:
        print(f"The grade {name} has received is: {grade}")
        break