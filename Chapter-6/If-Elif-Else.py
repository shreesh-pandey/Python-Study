# Lets write a program that calculates the incentives (% received on CTC) dependent on the Scorecard (Out of 10).
# The brackets are:
# Score greater than or equal to 9, Variable = 25%
# Score is between 6 and 8, Variable = 20%
# Score is between 3 and 5, Variable = 15%
# Score is less than 3, Variable = 10%

# Lets start with asking the name of the employee and his CTC.
emp_name = input("Enter the name of the employee: ")
emp_CTC = int(input("Enter the CTC of the employee: "))

# Now lets ask user to input the score for the employee.
emp_score = int(input(f"Input the score achieved for {emp_name}: "))

# Now lets calculate the variable for the employee.
if(emp_score >= 9):
    emp_variable = emp_CTC*0.25
    print(f"The variable pay for {emp_name} is: {emp_variable}")

elif(6<= emp_score <=8):
    emp_variable = emp_CTC*0.20
    print(f"The variable pay for {emp_name} is: {emp_variable}")

elif(3<= emp_score <=5):
    emp_variable = emp_CTC*0.15
    print(f"The variable pay for {emp_name} is: {emp_variable}")

else:
    emp_variable = emp_CTC*0.10
    print(f"The variable pay for {emp_name} is: {emp_variable}")