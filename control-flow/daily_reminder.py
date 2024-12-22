# daily_reminder.py

# Prompt for user input
task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ").strip().lower()
time_bound = input("Is the task time-bound? (yes or no): ").strip().lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"The task '{task}' is of HIGH priority."
    case "medium":
        reminder = f"The task '{task}' is of MEDIUM priority."
    case "low":
        reminder = f"The task '{task}' is of LOW priority."
    case _:
        reminder = "Invalid priority entered. Please use high, medium, or low."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " Immediate action is required as it is time-sensitive."

# Print the customized reminder
print(reminder)

