# Question 1: Merge Two Lists Alternately
# Scenario: You are developing a user interface where you need to display user names and their corresponding user IDs in an alternating fashion. You have two lists, one with user names and the other with user IDs. You need to merge them into a single list that alternates between names and IDs for display purposes.
#
# Example:
# User Names: ['Alice', 'Bob', 'Charlie']
# User IDs: [101, 102, 103]
# Merged List: ['Alice', 101, 'Bob', 102, 'Charlie', 103]

def merge_alternately(lst1, lst2):
    # Your code will go here
    pass

# How to test:
print(merge_alternately(['Alice', 'Bob', 'Charlie'], [101, 102, 103]))
# Expected output: ['Alice', 101, 'Bob', 102, 'Charlie', 103]
print(merge_alternately(['x', 'y'], [10, 20]))
# Expected output: ['x', 10, 'y', 20]


# Question 2: Find the Longest Word in a List
# Scenario: You are building a text analysis tool that processes a list of keywords extracted from user input. You need to identify the longest keyword to prioritize or highlight it in the output. This can help in emphasizing key terms that are more significant in a report or summary.
#
# Example:
# Keywords: ['data', 'analysis', 'machine', 'learning']
# Longest Keyword: 'machinelearning'

def longest_word(lst):
    # Your code will go here
    pass

# How to test:
print(longest_word(['data', 'analysis', 'machine', 'learning']))
# Expected output: 'learning'
print(longest_word(['sun', 'moon', 'stars']))
# Expected output: 'stars'


# Question 3: Sum of Squares of Numbers
# Scenario: You are developing a statistical analysis tool that calculates various metrics for a dataset. One of the metrics required is the sum of squares of values to compute variance. This helps in understanding the spread of data points from the mean.
#
# Example:
# Data Points: [2, 4, 6]
# Sum of Squares: 56 (2^2 + 4^2 + 6^2)

def sum_of_squares(lst):
    # Your code will go here
    pass

# How to test:
print(sum_of_squares([2, 4, 6]))
# Expected output: 56
print(sum_of_squares([1, 3, 5]))
# Expected output: 35


# Question 4: Find Common Elements in Two Lists
# Scenario: You are working on a feature that compares two lists of product IDs, one from an inventory system and the other from a sales report. You need to find the common product IDs to identify which products were both in inventory and sold during a given period.
#
# Example:
# Inventory IDs: [101, 102, 103]
# Sales IDs: [102, 104, 105]
# Common IDs: [102]

def common_elements(lst1, lst2):
    # Your code will go here
    pass

# How to test:
print(common_elements([101, 102, 103], [102, 104, 105]))
# Expected output: [102]
print(common_elements(['apple', 'banana'], ['banana', 'cherry']))
# Expected output: ['banana']


# Question 5: Count Occurrences of Each Character in a String
# Scenario: You are developing a text editor or a messaging app that needs to perform basic text analysis. For example, you want to analyze the frequency of each character in a user's message to detect patterns or common typing errors.
#
# Example:
# Message: "hello world"
# Character Counts: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

def count_characters(s):
    # Your code will go here
    pass

# How to test:
print(count_characters("hello world"))
# Expected output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
print(count_characters("Python programming"))
# Expected output: {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, ' ': 1, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 1}
