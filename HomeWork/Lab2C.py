# Class: CSE 1321L
# Section: 2C
# Term: Fall
# Instructor: John Blake
# Name: Limin Yang
# Lab#: 2C


w = float(input("Please enter a width: "))
h = float(input("Please enter a height: "))
P = (w + h) * 2
A = int(w * h)
formatted_number = "{:.2f}".format(A)
print(f"\033[1m{w}\33[1m")
print(f"\033[1m{h}\33[1m")
print("The perimeter is: ", P)
print("The area is: ",formatted_number)




