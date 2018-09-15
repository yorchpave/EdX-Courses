# Get the user to write 5 elements without repeting them and without 
# Entering blank answers
def get_names():

    user_list = []

    for user_input in range(5):

        user_input = input("Enter the name of an element: ")

        while(not user_input.strip(" ")):

            print("Input not valid")
            user_input = input("Enter the name of an element: ")
            
        while( user_input.lower() in user_list):

            print(user_input, "was already entered\t <--no duplicates allowed")
            user_input = input("Enter the name of an element: ")
        
        user_list.append(user_input.lower())

    return user_list

# Get the elements from the txt file and store them in a list
def get_elements():

    elements_list = []
    elements_file = open('elements1_20.txt', 'r') # Open file with read ability

    # Read first line of the file
    line = elements_file.readline()

    while line: # While there's a line to read
            element = line.strip('\n')
            elements_list.append(element.lower()) # Append current line to list
            line = elements_file.readline() # Check if there is another line to read
    
    elements_file.close() # Close file
    
    return elements_list

# Check the inputs from user and compare with elements in the list
# Store correct and incorrect answers, each in a separate list
# Get % of right answers and print it
# Print list of correct and incorrect answers 
def check_responses():

    correct_responses = []
    incorrect_responses = []
    for response in get_names():

        if(response in get_elements()):
            correct_responses.append(response.title())
        else:
            incorrect_responses.append(response.title())

    total_correct_responses = (len(correct_responses) / 5) * 100

    # Convert lists to strings for prettier output
    correct_responses_string = ' '.join(correct_responses)
    incorrect_responses_string = ' '.join(incorrect_responses)

    print(total_correct_responses, "%", "correct")
    print("Found: ", correct_responses_string)
    print("Not found: ", incorrect_responses_string)

print("List any 5 of the first 20 elements in the Period table\n")
check_responses()
    


