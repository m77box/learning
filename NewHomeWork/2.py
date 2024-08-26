# Question 2: Check if a Number is Prime
# Problem: Write a function is_prime(n) that takes an integer n and returns True if the number is prime, and False otherwise.

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False

        return True
    else:
        print("the number needs to be greater than 1.")

x = int(input("enter any number: "))
# How to test:
print(is_prime(x))   # Expected output: True
