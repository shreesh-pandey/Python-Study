# You are training for a space mission. As part of your mental focus training, you must count down by a certain step size.
# Write a program that:
    # Starts at a number chosen by the user
    # Ends at a target number (lower than the start)
    # Counts down in custom steps (like -1, -2, -5)

# Ex: If the user enters start = 10, end = 0, step = -2, it should print: 10, 8, 6, 4, 2, 0

# Lets start with a fun message.
print("Space mission countdown begins...")

# Now lets aski the user for 'Starting point', 'End Point' & 'Steps' for the countdown.
start = int(input("Please enter the Starting point for the countdown: "))
end = int(input("Please enter the End point for the countdown: "))
step = int(input("Please enter the Steps for the countdown: "))*-1  # '-1' as we need the negative countdown

print("Countdown sequence initiating ...")

for i in range(start, end-1, step):         # 'end-1' as the stop index stops at the final index.
    print(i)

print("Countdown complete! All systems go.")

# -------------------------- -------------------------- -------------------------- #

# Deep Dive:
# Above program currently runs only for negative countdown. However we can make it to work both ways.

# Lets start with a fun message.
print("Space mission countdown begins...")

# Now lets aski the user for 'Starting point', 'End Point' & 'Steps' for the countdown.
start = int(input("Please enter the Starting point for the countdown: "))
end = int(input("Please enter the End point for the countdown: "))
step = int(input("Please enter the Steps for the countdown: "))

if start > end:
    step = step*-1
else:
    step = step

print("Countdown sequence initiating ...")

for i in range(start, end - 1 if start > end else end + 1, step):
    print(i)

print("Countdown complete! All systems go.")

# -------------------------- -------------------------- -------------------------- #

# Another Example:
# Write a program that simulates a step counter for a fitness app.
# The user enters the number of steps they want to take in a day.
# Your program should count every step using a for loop and print motivational messages every few steps — e.g., every 1000 steps.
# You must use different versions of the range() function as needed.

# Lets start with setting a goal for the day. For that, we will ask the user for the numbers of steps.
# Step 1: Ask user for daily step goal
goal = int(input("Enter your step goal for today: "))

# Step 2: Simulate taking each step
print("Starting your step counter ...")

for step in range(1, goal + 1):
    if step % 1000 == 0:            # Give motivation every 1000 steps
        print(f"Great job! You’ve walked {step} steps!")

# Step 3: Congratulate at the end
print(f"Congratulations! You've completed your goal of {goal} steps!")

# -------------------------- -------------------------- -------------------------- #

# Deep Dive:
# This program can also be done with 'while' loop:
goal = int(input("Hi! Please enter your step goal for today: "))
steps_count = 0
milestone = int(input("Enter how often you'd like motivation (e.g., every 1000 steps): "))

print("🚶 Awesome! Let's start your session!\n")

while steps_count < goal:
    steps_count += 1
    if steps_count % milestone == 0:
        print(f"Congratulations! You've completed {steps_count} steps!")

print(f"Well done, you reached your goal of {goal} steps!")