# def add(v1,v2):
#     total = v1 + v2
#     return total
#
# def subtraction(v1,v2):
#         total = v1 - v2
#         return total
#
# def muliti(v1,v2):
#     total = v1 * v2
#     return total
#
# def div(v1,v2):
#     total = v1 / v2
#     return total
#
# def square(v1):
#     x = v1 **2
#
#     return x
#
#
# def squareroot(v1):
#     x = v1 ** 0.5
#
#     return x
#
#
# ## Call
# v1= int(input("enter a number: "))
# v2= int(input("enter a number: "))
# v3 =add(v1,v2)
# print(v3)
# v4 = subtraction(v1,v2)
# print(v4)
#
# v5 = muliti(v1,v2)
# print(v5)
#
# v6 = div(v1,v2)
# print(v6)
#
# v7 = square(v1)
# print(v7)
#
# v8 = squareroot(v1)
# print(v8)


#averge function  #avg
# level 1  , avg of 7  numbers
# v1= 9
# v2= 2
# v3= 2
# v4= 26
# v5= 2
# v6= 234
# v7 =18
#


# When a list is passed in a function it should return list of the square numbers
# inp = [1,2,4]
# x = [1,4,16]

array = [1,2,3,4]
def square(rainbow):
    s = []
    for i in rainbow:
        s.append(i**2)
    return s   #put the same line as "for" loop


print(array)
print(square(array))





