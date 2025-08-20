# . Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
myString = input("Enter your string: ")
freq = {}
for i in myString:
    freq[i] = freq.get(i, 0) + 1
print(freq)