# Control Statements 8.3.
# Write a series of statements that will take all of the characters in the original sentence, remove any duplicates,
# and return them in descending (Z -> A) order.

# 1st SOLUTION:

my_str = 'The quick brown fox jumps over the lazy dog'

my_list = []

for x in range(0, len(my_str)):
    y = my_str[x].upper()
    if y == ' ':
        continue
    elif y not in my_list:
        my_list.append(y)
        my_list.sort(reverse=True)
    else:
        pass
print(my_list)

# 2nd SOLUTION:


# def my_func(x):
#     return list(dict.fromkeys(x))


# my_sentence = 'The quick brown fox jumps over the lazy dog'
# my_list = my_func(my_sentence.upper().replace(' ', ''))
# my_list.sort(reverse=True)
# print(my_list)
