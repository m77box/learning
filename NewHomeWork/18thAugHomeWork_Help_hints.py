# try before you use Pseudocode's help

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


# Question 3: Find the Second Largest Number in a List
# Problem: Write a function second_largest(lst) that takes a list of numbers and returns the second largest number.
# Hint: Things that can be used: list, sorting, set, for loop, if-else statements

# More helpful hint:
# Consider sorting the list and then selecting the second largest element.

# Pseudocode:
# - Convert the list to a set to remove duplicates.
# - Sort the list in descending order.
# - Return the second element in the sorted list.


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


# Question 5: Calculate Factorial Using Recursion
# Problem: Write a function factorial(n) that takes an integer n and returns its factorial using recursion.
# Hint: Things that can be used: recursion, if-else statements, multiplication

# More helpful hint:
# The factorial of a number is the product of all positive integers less than or equal to that number.

# Pseudocode:
# - If n is 0 or 1, return 1.
# - Otherwise, return n multiplied by the factorial of (n-1).
