# Program to calculate and print the value of y based on the given expression

def calculate_expression():
    # Ask the user to enter an integer number
    x = int(input("Enter an integer value for x: "))
    
    # Calculate the value of y using the given expression
    y = x * x + 7 * x - 77 * x + 777 * x
    
    # Print the result
    print(f"The calculated value of y is: {y}")

# Call the function to run the program
calculate_expression()
