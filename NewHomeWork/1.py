# Question 1: Reverse a String
# Problem: Write a function reverse_string(s) that takes a string s and returns the string reversed.


def reverse_string(txt):
# return txt[::-1]
    str = ""
    for i in txt:
        str = i + str # for each character 'i', the function
    #prepends it to the string 'str'. This means that each new character is added to the front of str,
# effectively reversing the order of characters.
    return str

h = "helllo"

# How to test:
print("reversed result: ",reverse_string(h))  # Expected output: "olleh"

