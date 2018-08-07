# Ask user for input

fish_name = input("Enter fish name: ")
fish_price = input("Enter fish price (no symbols): ")

#fishstore fucntion with parameters and return value

def fishstore(fish, price):
    return "Fish Type: " + fish + " costs " + "$" + price

# Store function's return value in print_fishstore variable

call_fishstore = fishstore(fish_name, fish_price)
print(call_fishstore)