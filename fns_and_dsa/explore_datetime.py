# explore_datetime.py
from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date():
    """Calculates and displays the future date based on user input."""
    try:
        days_to_add = int(input("Enter the number of days to add: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future Date (after {days_to_add} days): {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

def main():
    """Main function to explore the datetime module."""
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()

