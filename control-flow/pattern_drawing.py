# Prompt user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Validate that the input is a positive integer
if size > 0:
    # Initialize row counter for while loop
    row = 0
    
    # Use a while loop to iterate through each row
    while row < size:
        # Use a for loop to print asterisks (*) side by side
        for col in range(size):
            print("*", end="")  # Print asterisk without newline
        print()  # Move to the next line after printing one row
        row += 1
else:
    print("Please enter a positive integer.")
