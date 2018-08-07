# Initialize input variable

user_input = ""

# Method that checks input and prints corresponding output

def str_analysis(user_input):

    # User can't leave space blank

    while user_input == "":
        user_input = input("Enter word or integer: ")
        if user_input != "":
            break
    if user_input.isdigit():  # If user input is digit, cast to int and check conditionals
        user_int = int(user_input)
        if user_int > 100:
            print("big number")
        elif user_int < 50:
            print("small number")
        else:
            print("nice number!")
    elif user_input.isalpha():  # If user input is alphabetic and check conditionals
        print("That's alphabetic!")
    else:
        print(user_input,"is an invalid input!")

# call str_analysis method

str_analysis(user_input)
