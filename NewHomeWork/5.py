# Question 5: Calculate Factorial Using Recursion
# Problem: Write a function factorial(n) that takes an integer n and returns its factorial using recursion.

# def factorial(n):
#     x=0
#     if n <=0:
#         print("done")
#     else:
#         print(n)
#         x = factorial(n-1)
#     return x
#
# y = 5
# # How to test:
# print(factorial(y))  # Expected output: 120



# print(factorial(3))  # Expected output: 6


# Also there are hard questions if you get dont with this
# BEST OF LUCK!

def factorial(n):
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n-1)  # Recursive case: n * factorial of n-1

y = 5
# How to test:
print(factorial(y))  # Expected output: 120

print(factorial(3))  # Expected output: 6

