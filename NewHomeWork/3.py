# Question 3: Find the Second Largest Number in a List
# Problem: Write a function second_largest(lst) that takes a list of numbers and returns the second largest number.

def second_largest(lst):
    # print(lst)
    l1 = {}
    num = 0
    new_l1 = sorted(lst, reverse=False)
    n =len(new_l1)-2
    return new_l1[n]




# # How to test:
# print(second_largest(l1))  # Expected output: 4

num = {9, 5, 4, 5,6,11,12,13}
print(second_largest(num))

# # How to test:
# print(second_largest(l1))  # Expected output: 4
