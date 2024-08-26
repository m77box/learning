# Question 1: Reverse a String
# Problem: Write a function reverse_string(s) that takes a string s and returns the string reversed.

def reverse_string(s):
    return s[::-1]


txt = "hello"
# How to test:
print(reverse_string(txt))  # Expected output: "olleh"


# j =[5 ,7, 9, 9] #set
# print(type(j))
#
# h = list(j)

# c = float(input("enter temp(c): "))
# temp = ((9.5/5.0) * c + 32)
# print("temp in f: " + str(temp))
# temp = int(temp/10)
# match (temp):
#     case 10:
#         print("too hot")
#     case 9:
#         print("still hot")
#     case 1:
#         print("cold")
#     case _:
#         print("too cold")

# if __name__ == "__main__":  #question...
#
#     zone = input("enter the zone: ")
#     weight = int(input("weight: "))
#
# match (zone):
#     case domestic:
#         if weight <= 5:
#             print("the cost is 5")
#         elif 5 < weight <= 20:
#             print("the cost is 10")
#         else:
#             weight > 20
#             print("the cost is 15")


if __name__ == "__main__"