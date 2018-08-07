import sys # Import so user can quit program

# Initialize input variable so function
# Can be called by passing argument

user_input = ""

# Function that makes the adding report

def adding_report(input_type):

    total = 0 # Initialize variable so total amount can be calculated

    while True:  # Constantly ask user in case of invalid first input

        input_type = input("Choose Report Type (\"A\" or \"T\"): ")

        # Case user inputs A

        if input_type.upper() == "A":
            input_list = "" # Initialize variable where list of items will be stored
            while True: # Constantly ask user for an integer or quit program
                
                integer_input = input("Enter an integer or \"Q\": ")
                if integer_input.isdigit():
                    input_list += integer_input + "\n" # Add string input to input_list
                    input_total = int(integer_input) # Cast so input can be summed for total
                    total += input_total
                elif integer_input.upper().startswith("Q"):  # Print statements when user quits program
                    print("\nItems:")
                    print(input_list)
                    print("Total")
                    print(total)
                    sys.exit(0)              
                else:
                    print("Try again.")

        # Case user inputs T

        if input_type.upper() == "T":

            while True:

                integer_input = input("Enter an integer or \"Q\": ")
                if integer_input.isdigit():
                    input_total = int(integer_input)
                    total += input_total
                elif integer_input.upper().startswith("Q"):  
                    print("\nTotal")
                    print(total)
                    sys.exit(0)               
                else:
                    print("Try again.")
        else:
            print("Try again.")
                    
    

# Call function passing string argument

adding_report(user_input)
        

