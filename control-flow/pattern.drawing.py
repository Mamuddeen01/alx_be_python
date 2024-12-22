# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Ensure the input is a positive integer
if size <= 0:
    print("Please enter a positive integer.")
else:
    # Use a while loop to iterate through each row
    row = 0
    while row < size:
        # Use a for loop to print asterisks for each column
        for col in range(size):
            print("*", end="")  # Print asterisk without a newline
        print()  # Print a newline after completing the row
        row += 1

