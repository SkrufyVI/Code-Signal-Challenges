'''
Write a function that checks for a palindrome.
Return True or False.
'''


def checkPalindrome(inputString):
    reversed_inputstring = "".join(reversed(inputString))
    if reversed_inputstring == inputString:
        inputString = True

    else:
        inputString = False

    return inputString

print(checkPalindrome("john"))
