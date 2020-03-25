
balloon = "john"
reversed_baloon = "".join(reversed(balloon))
print(reversed_baloon)



def checkPalindrome(inputString):
    reversed_inputstring = "".join(reversed(inputString))
    if reversed_inputstring == inputString:
        inputString = True

    else:
        inputString = False

    return inputString

print(checkPalindrome("john"))
