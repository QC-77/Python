# Program to read a file and return a list of lines without newline characters

def read_file_to_list(filename):
    try:
        # Open the file for reading
        with open(filename, 'r') as file:
            # Read all lines, strip newline characters, and store them in a list
            lines = [line.strip() for line in file]
        
        # Return the list of cleaned lines
        return lines
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Entry point for the program
if __name__ == "__main__":
    # Ask the user for the filename
    filename = input("Enter the filename (with extension): ")
    
    # Call the function and store the result
    result = read_file_to_list(filename)
    
    # Check if the result is not empty and print the list
    if result:
        print("The file content as a list:")
        print(result)
    else:
        print("No data was returned or the file could not be read.")
