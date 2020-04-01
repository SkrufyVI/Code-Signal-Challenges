# Given an array of integers, find the pair of adjacent elements that has the largest product;
# Return that product.

# For input_array = [3,6,-2,-5,7,3], the output should be 21,
# Because 7 and 3 produce the largest product.

# Method 1, uses the in-builty Python sort function.


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

# Method 2, More important to remember, as it doesn't abuse the sort function. 
# Will be more useful for less friendly languages.

def largest_adjacent_product(numbers):


    largest_product = 0
    for i in range(0, len(numbers) - 1):
        product = numbers[i] * numbers[i + 1]
        if product > largest_product:
            largest_product = product

    return largest_product



