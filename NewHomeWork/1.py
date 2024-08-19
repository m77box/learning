# Question 1: Reverse a String
# Problem: Write a function reverse_string(s) that takes a string s and returns the string reversed.


def reverse_string(txt):
    return txt[::-1]

h = input("enter a txt: ")

# How to test:
print("reversed result: ",reverse_string(h))  # Expected output: "olleh"
