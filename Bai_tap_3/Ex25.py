# 25. Write a Python program to create a Caesar encryption.
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's
# code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a
# type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed
# number of positions down the alphabet. For example, with a left shift of 3, D would be replaced
# by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his
# private correspondence.

def ceasar_encryption(plaintext, key):
    key = key % 26
    ciphertext = ""
    for c in plaintext:
        if c.isalpha():
            if c.islower():
                ciphertext += chr((ord(c) - ord('a') + key) % 26 + ord('a'))
            if c.isupper():
                ciphertext += chr((ord(c) - ord('A') + key) % 26 + ord('A'))
        else:
            ciphertext += c
    return  ciphertext

plaintext = input("Enter your plaintext: ")
key = int(input("Enter your key: "))
print(ceasar_encryption(plaintext, key))
