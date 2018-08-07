# Declare variables

quote = input("Enter a 1 sentence quote, non-alpha separate words: ")
word = ""
quote_length = len(quote)
length_counter = 0

# Loop through each character in quote given

for character in quote:

    if(character.isalpha()): # Check if character is alphabetic
        word += character # If so, add char to string word
        length_counter += 1 
    
    elif(len(word) == 0): # In case of space after a comma
        length_counter += 1
        


    elif(word[0].lower() >= 'h'): 
        length_counter += 1
        print(word.upper())
        word = ""
    
    elif(word[0].lower() < 'h'): 
        length_counter += 1
        word = ""
    
    if (length_counter == quote_length): # Check if the loop is over

        if(word[0].lower() >= 'h'):
            print(word.upper())
    
    
            
    
