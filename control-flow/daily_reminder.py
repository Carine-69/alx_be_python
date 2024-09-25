task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound=input("Is it time-bound? (yes/no): ").lower()
match priority:
    case "high":
        if time_bound=="yes":
            print("Reminder: " +"'"+task + "'"+" is a high priority task that requires immediate attention today!")
    case "medium":
         if time_bound=="no":
            print("Note: "+"'"+task + "'"+" is a medium priority task. Consider completing it when you have free time")
    case "low":
        if time_bound=="no":
            print("Note: "+"'"+task + "'"+ " is a low priority task. Consider completing it when you have free time")