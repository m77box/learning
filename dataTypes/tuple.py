# tuple = ("history", "math", "english")
# tuple1 = tuple
#
# tuple[0] = 'art'
#
# print(tuple)
# print(tuple1)
#
# #-------------
# # "sets" is unorder and no duplicates and uses {} "curly brackets",
# # "sets" do more efficiently than "tuple" such it can check the same value
# # in two lists by using .intersection and check on difference value by useing
# # .difference
#
# courses = {'history' , 'math', 'english', 'math'}
# art_courses = {'history', 'math', 'art'}
#
#
# print(courses.intersection(art_courses))
# print(art_courses.union(courses))

#--------------------------
# Empty Lists
# empty_list = []
# # or
# empty_list = list() # list() is a built-in list class
#
# # Empty Tuples
# empty_tuple = ()
# empty_tuple = tuple()
#
# # Empty Sets
# empty_set ={} # this is INCORRECT because it is a dictionary
# empty_set = set()


def process_numbers(numbers):
    results = []
    for number in numbers:
        number_str = str(number)
        if number % 2 == 0:
            results.append(number_str + " is even")
        else:
            results.append(number_str + " is odd")

    for result in results:
        print(result)

input_numbers = [3,5,6,7,8,9]


# Example usage:
if __name__ == "__main__":
    print("Limin is learning git")
    pass