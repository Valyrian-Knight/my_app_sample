# Control Statements 8.3.
# Write a series of statements that will take all of the characters in the original sentence, remove any duplicates,
# and return them in descending (Z -> A) order.

# 1st SOLUTION:

user_string = input('Please, enter a sentence: ')

#user_string = 'The quick brown fox jumps over the lazy dog'

new_list = []

for start_indx in range(0, len(user_string)):
    mov_indx = user_string[start_indx].upper()
    if mov_indx == ' ':
        continue
    elif mov_indx not in new_list:
        new_list.append(mov_indx)
        new_list.sort(reverse=True)
    else:
        pass
print(new_list)

#2nd SOLUTION(using list(dict)):

# def my_func(x):
#     return list(dict.fromkeys(x))


# my_sentence = 'The quick brown fox jumps over the lazy dog'
# my_list = my_func(my_sentence.upper().replace(' ', ''))
# my_list.sort(reverse=True)
# print(my_list)
