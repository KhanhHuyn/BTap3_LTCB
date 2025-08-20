# 12. Write a Python program to count the occurrences of each word in a given sentence.

myString = input("Enter your string: ")
wordList = myString.split(" ")
wordFreq = {}
for word in wordList:
    wordFreq[word] = wordFreq.get(word, 0) + 1
print("The occurrence of each word in your string:", wordFreq)
