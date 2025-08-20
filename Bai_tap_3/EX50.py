# 50. Write a Python program to split a string on the last occurrence of the delimiter.
def split_on_last(s, delimiter):
    parts = s.rsplit(delimiter, 1)
    return parts


my_string = input("Enter your string: ")
delimiter = input("Enter your delimiter: ")
print(split_on_last(my_string, delimiter))