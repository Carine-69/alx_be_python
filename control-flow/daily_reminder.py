# Prompt the user to enter their task, priority, and whether it's time-bound
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to handle different priority levels
match priority:
    case 'high':
        message = f"Reminder: '{task}' is a high priority task"
    case 'medium':
        message = f"Reminder: '{task}' is a medium priority task"
    case 'low':
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = "Invalid priority input."

# Check if the task is time-bound and modify the message accordingly
if time_bound == 'yes':
    message += " that requires immediate attention today!"
elif time_bound == 'no':
    message += ". Consider completing it when you have free time."

# Output the customized reminder
print(message)
