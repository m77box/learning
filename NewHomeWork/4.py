
# Question 4: Count Vowels in a String
# Problem: Write a function count_vowels(s) that takes a string s and returns the number of vowels (a, e, i, o, u) in the string.

def count_vowels(s):
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    numbers_vowel = 0
    for i in s:
        if i in vowel:
           numbers_vowel += 1
    return numbers_vowel
    # check Pseudocode from file 18thAugHomework_Help*.py

x = "limin"
# How to test:
print("this text contains total vowels are: ", count_vowels(x))  # Expected output: 3
