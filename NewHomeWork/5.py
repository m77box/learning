# Question 5: Calculate Factorial Using Recursion
# Problem: Write a function factorial(n) that takes an integer n and returns its factorial using recursion.


# how many ways to solve problem, there are 5000 ways to solve problem
def factorial(n):
    l =[]
    while n>0:
        l.append(n)
        n = n - 1
        print(n)
    total = 1
    for i in l:
        total = total * i
    return total



y = 5
# How to test:
print(factorial(y))  # Expected output: 120

# print(factorial(3))  # Expected output: 6


# Also there are hard questions if you get dont with this
# BEST OF LUCK!

# limin = []
# print(limin)
# limin.append('string called smart limin')
# print(limin)
# limin.append('string called not so smart limin')
# print(limin)
# limin.append(6)
# print(limin)
# limin.append('6')
# print(limin)
# rutvik = ['not','so','smart']
# limin.append(rutvik)
# print(limin)
# rutvik = {'not':'so'}
# limin.append(rutvik)
# print(limin)
# for i in limin:
#     print(i)
#     print(type(i))
#
