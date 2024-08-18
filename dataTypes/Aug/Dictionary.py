# # Basic Dictionary Creation:
# #
# # How do you create an empty dictionary in Python?
#
# h = {}
#
# # Create a dictionary called student with the keys name, age, and grade, and appropriate values.
# u = {'name': "john", 'age' : 18, 'grade': 'junior' }
# # Accessing Values:
# #
student = {'name': 'John', 'age': 21, 'grade': 'A'}
# #how would you access the value associated with the key name?
#
# print(student['name'])
#
# # What will happen if you try to access a key that does not exist in the dictionary?
# print(student.get('phone', "not found"))
#
# # Updating and Adding Items:
# student['sing'] = 'song'
# print(student)
#
# # How do you update the value of the key 'grade' in the dictionary student to 'B'?
# student['grade'] = 'B'
# print(student['grade'])
#
# # How do you add a new key-value pair {'major': 'Computer Science'} to the dictionary?
# student['major'] = 'computer science'
# print(student)
#
# # Removing Items:
# # How do you remove the key 'age' from the dictionary student?
# student.pop('age')
# print(student)

# What does the get() method do in a dictionary, and how is it different from directly accessing a key?
# student.get('e','not found')

# # Explain the purpose of the keys(), values(), and items() methods.
# x = student.items()
# for k,v in student.items():
#     print(k,v)

# Looping Through a Dictionary:
# loop that prints each key-value pair in the dictionary student.
for i in student.items():
    print(i)


# How can you loop through only the keys of a dictionary? How about only the values?
# Checking for Keys:
# for ki,vi in student.items():
#     print(vi)

# What is a dictionary comprehension? Write a comprehension that creates a dictionary with keys as numbers from 1 to 5 and values as their squares.
# Merging Dictionaries:

#
# Given two dictionaries dict1 = {'a': 1, 'b': 2} and dict2 = {'b': 3, 'c': 4}, how do you merge them into one dictionary?
# Common Errors:
#
# What error will you get if you try to access a key that does not exist in a dictionary? How can you avoid this error?
# What happens if you use an unhashable type (like a list) as a key in a dictionary?
# These questions cover key aspects of dictionary usage in Python and can help assess the students' understanding of this fundamental data structure.