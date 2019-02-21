some_string = 'nokaz ej trebor cijnoj'


def reverse_a_string_more_slowly(a_string):
    new_strings = []
    index = len(a_string)
    while index:
        index -= 1
        new_strings.append(a_string[index])
    return ''.join(new_strings)


rev_string = reverse_a_string_more_slowly(some_string)
print(rev_string)
