# Declare variables

user_input = input("Enter a saying or poem: ")

words_list = user_input.split()

words_list_length = len(words_list)

# Function that sorts given list, creates a new one. If given list
# is bigger than 5 elements, it pops first, last, and fifth from 
# last (-5). Then, add those popped elements to list created
# until given list >= 5

def word_mixer(words_list):

    words_list.sort()

    final_list = []

    if(len(words_list) <= 5):

        final_list = words_list 


    else:

        while(len(words_list) > 5):

            first_word_popped = words_list.pop(-5)

            final_list.append(first_word_popped)
        
            second_word_popped = words_list.pop(0)
            
            final_list.append(second_word_popped)

            third_word_popped = words_list.pop(-1)

            final_list.append(third_word_popped)

            final_list.append(" ")
   
    return final_list


for item in range(len(words_list)): # Iterate through string (casted to list) given by user

    if(len(words_list[item]) <= 3): # user_list[item] = current word

        words_list[item] = words_list[item].lower()

    elif(len(words_list[item]) >= 7):

        words_list[item] = words_list[item].upper()


new_words = word_mixer(words_list) # Store return value in a variable

print(new_words) # Print return value through variable

