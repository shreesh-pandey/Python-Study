# Q.3: Write a Python program to check whether a student has passed or failed. The passing rules are:
#           - There are five subjects: Mathematics, Physics, Chemistry, English, Hindi.
#           - The student must score at least 33% in each of the five subjects
#           - The average percentage of all three subjects must be 40% or more
#     Ask the user to enter marks for 5 subjects (out of 100), and then print whether the student has Passed or Failed.

# Lets start with asking the user to input the name of the Student.
name = input("Please enter the name of the student: ")

# Now, lets ask the user to input the marks in each subjects.
mathematics = int(input(f"Please enter the marks {name} received in Mathematics: "))
physics = int(input(f"Please enter the marks {name} received in Physics: "))
chemistry = int(input(f"Please enter the marks {name} received in Chemistry: "))
english = int(input(f"Please enter the marks {name} received in English: "))
hindi = int(input(f"Please enter the marks {name} received in Hindi: "))

# Lets calculate the overall percentage the student has received.
percentage = (mathematics+physics+chemistry+english+hindi)/5

# Lets check the status of the student as per the conditions mentioned in the question.
if (
    mathematics >= 33 and
    physics >= 33 and
    chemistry >= 33 and
    english >= 33 and
    hindi >= 33 and
    percentage >= 40
    ):
        print(f"Congratulations! {name} has Passed! The percentage received is: {percentage}")
else:
        print(f"Sorry! {name} has not Passed! The percentage received is: {percentage}")

# Deep Dive:
# Another (a bit advanced) way to solve this is by using lists and dictionaries.

# Step 1: Ask the user to enter the student's name
name = input("Please enter the name of the student: ")

# Step 2: Create a list of subjects and an empty dictionary to store marks
subjects = ["Mathematics", "Physics", "Chemistry", "English", "Hindi"]
marks = {}  # This will store each subject as a key and the marks as its value

# Step 3: Ask the user to input marks for each subject
for subject in subjects:    # The for loop goes through each subject in the 'subjects' list
    # For each subject, ask the user to enter the marks and stores it in the 'marks' dictionary with subject name as the key
    marks[subject] = int(input(f"Please enter the marks {name} received in {subject}: "))

# Step 4: Calculate the total and percentage
total_marks = sum(marks.values())               # Adds all the marks entered
percentage = total_marks / len(subjects)        # Divides total by number of subjects (5)

# Step 5: Check if the student passed in all subjects and overall
passed_all_subjects = all(mark >= 33 for mark in marks.values())    # 'all()' checks if every mark is greater than or equal to 33

# Check if the average percentage is at least 40%
passed_overall = percentage >= 40

# Step 6: Show final result based on both conditions
if passed_all_subjects and passed_overall:
    print(f"Congratulations! {name} has Passed! The percentage received is: {percentage:.2f}%")  # .2f ensures the output shows 2 decimal places, like 97.80%.
else:
    print(f"Sorry! {name} has Failed. The percentage received is: {percentage:.2f}%")


    