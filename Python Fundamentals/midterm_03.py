user_input = input("Enter a saying or poem:\n") # Ask user for input

words_list = user_input.split() # Split user input into array

words_list_length = len(words_list) # Get array length

# Function that sorts given list, creates a new one. If given list
# is bigger than 5 elements, it pops first, last, and fifth from 
# last (-5). Then, add those popped elements to list created
# until given list >= 5

def word_mixer(words_list):

    words_list.sort()

    final_list = ""

    if(len(words_list) <= 5):

        final_list = words_list 


    else:

        while(len(words_list) > 5):

            first_word_popped = words_list.pop(-5)

            final_list += first_word_popped + " "
        
            second_word_popped = words_list.pop(0)

            final_list += second_word_popped + " "

            third_word_popped = words_list.pop(-1)
            
            final_list += third_word_popped + "\n" 
   
    return final_list

# For loop that iterates though every item
# in the list and changes to upper if
# item >=7 and lowers if item <= 3
for item in range(len(words_list)): 
    if(len(words_list[item]) <= 3): 

        words_list[item] = words_list[item].lower()

    elif(len(words_list[item]) >= 7):

        words_list[item] = words_list[item].upper()

# Store the return value of word_mixer function
# in new varaiable
new_words = word_mixer(words_list) 

print()
print(new_words) # Print new variable

