# Given an array of integers, find the pair of adjacent elements that has the largest product;
# Return that product.

# For input_array = [3,6,-2,-5,7,3], the output should be 21,
# Because 7 and 3 produce the largest product.


# What I want is an iterator that can loop:
# index[0] x index[1], index[1] x [index[2], index[2] x index[3]
# until index[-2] x index[len]

# What if we create two duplicates of the same list?


def adjacentElementsProduct(inputArray):
    array_1 = inputArray
    array_2 = array_1
    list_length = len(array_1)
    product = []

    for i in range(0, list_length-1):
        product.append(array_1[i] * array_2[i + 1])

    product.sort()
    answer = product[-1]
    return answer


test_array = [3, 6, -2, -5, 7, 3]
print(adjacentElementsProduct(test_array))



def largest_adjacent_product(numbers):
    '''
    This is an important pattern to know
    '''

    largest_product = 0
    for i in range(0, len(numbers) - 1):
        product = numbers[i] * numbers[i + 1]
        if product > largest_product:
            largest_product = product

    return largest_product

'''
[1,2,3,4,5]

largest_product = 0
i iterates until 4:
        product = numbers[0] * numbers[0 + 1]
        if product > largest_product:
                largest_product = product

'''

# Basically, largest_product keeps getting a new figure every time there is a max multiple sum.
# If the new
# Largest_product keeps updating every time the multiplication gets larger.
# No need for a cheating sort function, this is the sort function.

