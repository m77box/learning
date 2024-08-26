# Question 1: Reverse a String
# Problem: Write a function reverse_string(s) that takes a string s and returns the string reversed.
# Hint: Things that can be used: list, len, slicing, for loop, string concatenation

# More helpful hint:
# Think about how you can convert the string into a list of characters to reverse it.

# Pseudocode:
# - Convert the string into a list of characters.
# - Reverse the list.
# - Join the characters back into a string.
# - Return the reversed string.

def reverse_string(s):
    # Convert the string into a list of characters
    chars = list(s)
    # Reverse the list
    chars.reverse()
    # Join the characters back into a string
    reversed_string = ''.join(chars)
    return reversed_string

# How to test:
print(reverse_string("hello"))  # Expected output: "olleh"
print(reverse_string("Python"))  # Expected output: "nohtyP"


# Question 2: Check if a Number is Prime
# Problem: Write a function is_prime(n) that takes an integer n and returns True if the number is prime, and False otherwise.
# Hint: Things that can be used: for loop, range, modulus operator %, if-else statements

# More helpful hint:
# A prime number has no divisors other than 1 and itself.

# Pseudocode:
# - If n is less than 2, return False.
# - Loop from 2 to the square root of n:
#   - If n is divisible by any number in this range, return False.
# - If no divisors are found, return True.

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# How to test:
print(is_prime(7))   # Expected output: True
print(is_prime(10))  # Expected output: False


# Question 3: Find the Second Largest Number in a List
# Problem: Write a function second_largest(lst) that takes a list of numbers and returns the second largest number.
# Hint: Things that can be used: list, sorting, set, for loop, if-else statements

# More helpful hint:
# Consider sorting the list and then selecting the second largest element.

# Pseudocode:
# - Convert the list to a set to remove duplicates.
# - Convert the set back to a list.
# - Sort the list in descending order.
# - Return the second element in the sorted list.

def second_largest(lst):
    unique_lst = list(set(lst))  # Remove duplicates
    unique_lst.sort(reverse=True)  # Sort in descending order
    return unique_lst[1]  # Return the second largest element

# How to test:
print(second_largest([1, 2, 3, 4, 5]))  # Expected output: 4
print(second_largest([10, 10, 5, 3]))   # Expected output: 5


# Question 4: Count Vowels in a String
# Problem: Write a function count_vowels(s) that takes a string s and returns the number of vowels (a, e, i, o, u) in the string.
# Hint: Things that can be used: list, for loop, if-else statements, lower() method, in operator

# More helpful hint:
# Convert the string to lowercase and count the vowels.

# Pseudocode:
# - Convert the string to lowercase.
# - Initialize a counter for vowels.
# - Loop through each character in the string:
#   - If the character is a vowel, increment the counter.
# - Return the counter.

def count_vowels(s):
    vowels = "aeiou"
    s = s.lower()  # Convert string to lowercase
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# How to test:
print(count_vowels("hello world"))  # Expected output: 3
print(count_vowels("Python"))       # Expected output: 1


# Question 5: Calculate Factorial Using Recursion
# Problem: Write a function factorial(n) that takes an integer n and returns its factorial using recursion.
# Hint: Things that can be used: recursion, if-else statements, multiplication

# More helpful hint:
# The factorial of a number is the product of all positive integers less than or equal to that number.

# Pseudocode:
# - If n is 0 or 1, return 1.
# - Otherwise, return n multiplied by the factorial of (n-1).

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# How to test:
print(factorial(5))  # Expected output: 120
print(factorial(3))  # Expected output: 6
