# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the rows
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks side by side in each row
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Print newline after each row to move to the next line
    row += 1  # Move to the next row
