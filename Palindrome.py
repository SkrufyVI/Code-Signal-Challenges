'''
Write a function that checks for a palindrome.
Return True or False.
'''

# Method

def checkPalindrome(inputString):
    reversed_inputstring = "".join(reversed(inputString))
    if reversed_inputstring == inputString:
        inputString = True

    else:
        inputString = False

    return inputString

print(checkPalindrome("john"))

# The above method abuses the Python inbuilt Python reverse function.
# To reverse a string without this function, see below function:
# Basically, create a list with the same length, and then fill it in backwards.

def reverse_string(my_string):
    a_list = list(my_string) 
    list_length = len(a_list) 
    b_list = [""] * list_length 

    for i in range(0, list_length): 
        b_list[i] = a_list[(list_length - i) - 1]
       
    return "".join(b_list) 

