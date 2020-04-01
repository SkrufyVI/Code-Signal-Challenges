'''
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.
'''

'''
n = 123456
i = [int(x) for x in str(n)]
# This list comprehension was the key to solving this. Saving it here for later.
# You can't use list(n), as the computer doesn't know where to break the list.
'''

def isLucky(n):
    ticket = [int(number) for number in str(n)]
    half = int(len(ticket)/2)
    i = (ticket[0: half])
    j = (ticket[half:])
    if sum(i) == sum(j):
        return True
    else:
        return False






