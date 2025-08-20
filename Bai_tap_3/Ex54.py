def first_repeated_char(s):
    chars_dict = {}
    for c in s:
        if c not in chars_dict:
            chars_dict[c] = 1
        else:
            chars_dict[c] += 1

    for c in s:
        if chars_dict[c] == 2:
            return c

    return None


my_string = input("Enter your string: ")
print(first_repeated_char(my_string))