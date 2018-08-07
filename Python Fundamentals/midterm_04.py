user_input = input("Enter a saying or poem: ")

words_list = user_input.split()

words_list_length = len(words_list)


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
   
    return final_list


for item in range(len(words_list)): 
    if(len(words_list[item]) <= 3): 

        words_list[item] = words_list[item].lower()

    elif(len(words_list[item]) >= 7):

        words_list[item] = words_list[item].upper()


new_words = word_mixer(words_list) 

print(new_words) 


my_list = ["John", "Mary", "George", "Michael", "Phillip", "Will", "William", "Walter", "Bob"]

print(my_list)
