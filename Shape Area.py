'''
# Below we will define an N- interesting polygon;
# Your task is to find the area of a polygon for a given n;
# A 1- interesting polygon is just a square with a side of length 1;
# An n- interesting polygon is obtained by taking the n-1 interesting polyton and appending 1- interesting polygons 
to its rim, side by side;
# For n=2, the output should be shapeArea(n) = 5
# For n=3, the output should be shapeArea(n) = 13
'''

# Method 1. It's a quadratic equation, so can be done on paper then typed up:


def shapeArea(n):
    answer = 2 * n**2 - 2 * n + 1
    return answer

print(shapeArea(3))
print(shapeArea(4))

# Method 2. Derived this pattern from looking at a few case studies

def count_area_by_looping(n):
	increase = 0
	area = 1
	for i in range(0, n):
		area += increase #area is = area + increase
		increase += 4 #increase = increase + 4
	return area




