task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")

# match priority :
# case time:
if priority == "high" and time== "yes":
    print(f"Finish '{task}' is a high priority task that requires immediate attention today!") 
elif priority == "medium" and time == "yes":
    print(f"Finish '{task}' is a medium priority task that requires immediate attention today!")
elif priority == "medium" and time == "no":
    print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
else:
    print("you got no priorities today")