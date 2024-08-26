# Question 5: Calculate Factorial Using Recursion
# Problem: Write a function factorial(n) that takes an integer n and returns its factorial using recursion.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)



y = 5
# How to test:
print(factorial(5))  # Expected output: 120

