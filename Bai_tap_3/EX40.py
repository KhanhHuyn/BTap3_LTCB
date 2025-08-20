# 40. Write a Python program to reverse words in a string
my_string = input("Enter your string: ")
words = my_string.split(" ")
for i in range(len(words)):
    words[i] = words[i][::-1]
reversed_word_string = " ".join(words)
print(reversed_word_string)