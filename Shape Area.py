# A computer language is mathematical

# Below we will define an N- interesting polygon;
# Your task is to find the area of a polygon for a given n;
# A 1- interesting polygon is just a square with a side of length 1;
# An n- interesting polygon is obtained by taking the n-1 interesting polyton and appending 1- interesting polygons to its rim, side by side;
# For n=2, the output should be shapeArea(n) = 5
# For n=3, the output should be shapeArea(n) = 13

# Quadratic equation = 2 * n**2 - 2 * n + 1


def shapeArea(n):
    answer = 2 * n**2 - 2 * n + 1
    return answer

print(shapeArea(3))
print(shapeArea(4))


# The increase of the area goes up by 4 every time
# Derived this pattern from looking at a few case studies

def count_area_by_looping(n):
	increase = 0
	area = 1
	for i in range(0, n):
		area += increase #area is = area + increase
		increase += 4 #increase = increase + 4
	return area

'''
n = 1, 1 iteration:
area = 1
increase = 4
return = 1, correct

n = 2, 2 iterations
...
area = 5 (1+4)
increase = 8 (4+4)
return = 5, correct

n = 3, 3 iterations
...
...
area = 13 (5+8)
increase = 12 (8+4)
return = 13, correct

n = 4, 4 iterations
...
...
...
area = 25 (13 + 12) 
increase = 16 (12 + 4)
return = 25, correct

n = 5, 5 iterations
...
...
...
...
area = 41 (25 + 16)
increase = 20 (16 + 4)
return = 41, correct

'''







