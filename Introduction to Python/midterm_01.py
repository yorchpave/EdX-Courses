# Ask user for input 

input_test = input("Enter food categories eaten in past 24 hrs: ").lower()

# Check for specific food category

check_for_dairy = "dairy" in input_test
check_for_nuts = "nuts" in input_test
check_for_Seafood = "Seafood".lower() in input_test
check_for_chocolate = "chocolate" in input_test

# Print statements

print('It is',check_for_dairy,'that "' + input_test + '" contains "dairy"')
print('It is',check_for_nuts,'that "' + input_test + '" contains "nuts"')
print('It is',check_for_Seafood,'that "' + input_test + '" contains "seafood"')
print('It is',check_for_chocolate,'that "' + input_test + '" contains "chocolate"')
