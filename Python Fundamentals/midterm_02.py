import sys # import so user can quit the program

current_list = ["cat", "goat", "cat"] # Initialize list of animals

# Function that returns different states of list
# Depending on the user input

def list_o_matic(user_input):

    if(user_input == ""):
        current_list.pop()
        print("Last instance popped from list\n")

    elif(user_input in current_list):
        current_list.remove(user_input)
        print("1 instance of", user_input, "removed from list\n")
            
    else:
        current_list.append(user_input)
        print("1 instance of", user_input, "appended to list\n")

    return current_list



while current_list: # While list is populated

    print("Look at all the animals", current_list) 

    user_input = input("Enter the name of an animal: ")

    if(user_input.lower() == "quit"):
        sys.exit(0)
    else:
        list_o_matic(user_input)














