'''
Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

Example

For year = 1905, the output should be
centuryFromYear(year) = 20;
For year = 1700, the output should be
centuryFromYear(year) = 17.
'''

import math
# print(math.ceil(15.82))


def century_from_year(year):
    if(year % 100 != 0):
        divided_century = year/100
        correct_century = math.ceil(divided_century)
        return correct_century
    if(year % 100 == 0):
        divided_century = year/100
        correct_century = int(divided_century)
        return correct_century

print(century_from_year(1700))
