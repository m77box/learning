#contain "main", which is the entry/starting point of the program

# if __name__ == "__main__":
#     print('hello, world!')
#     print('bob'+' was'+' here.', end='')  #the spacing before a line is mandatory!
#
# if __name__ == '__main__':
#     x = input("please enter your name: ")
#     print('hello,' + x)
#
# if __name__ == '__main__':
#     userInput = input('please enter your age: ')
#     print('You are ' + userInput + ' years old.')
#     pass


# Addtion (+)
# subtraction(-)
# mulitiplicaiton(*)
# power(**)
# division(/)
# floor division(//)
# modulus(%)

# weight = float(input('please enter your weight in pounds: '))
# moon_weight = round(16.5/100 * weight, 2)
#
# print(f'your moon weight is', moon_weight,'lb')

#
# t = float(input('please enter the temperature in Fahrenheit: '))
# formula = (t - 32)*5/9 + 273.15
# print('Kevin temperature is ', formula)

# x = 1
# x += 8 #(x = x + 8) is the same type of calculation
# print(x)


#from library import the feature from the library
from random import random, seed
seed(10)
n = random()
print(n)