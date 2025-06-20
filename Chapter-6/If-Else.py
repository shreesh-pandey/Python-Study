# Lets make a program that uses if-else statement to check if a user is eligible for pension or not.

# Lets start with asking the user to input the name and age.
name = input("Enter the name of the user: ")
age = int(input("Enter the age of the user: "))

# Since, the retirement age is usually 60, hence if the age => 60, the person is eligible.
if(age>=60):
    print(name, "is eligible for Pension! Congratulations & enjoy your retirement!")
else:
    print(name, "is not eligible for Pension! Congratulation! You can stay on the job & keep up the good work!")
