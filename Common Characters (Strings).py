'''
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
'''



def commonCharacterCount(s1, s2):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    s1 = list(s1)
    s2 = list(s2)
    counter = 0
    for l in alphabet:
        if l in s1 and s2:
            i = s1.count(l)
            j = s2.count(l)
            if i > j:
                commonality = j
            elif j > i:
                commonality = i
            else:
                commonality = i
            counter += commonality
    return(counter)

