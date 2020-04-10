'''

Some people are standing in a row in a park.
There are trees between them which cannot be moved.
Your task is to rearrange the people by their heights in a non-descending order without moving the trees.

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190]

'''

# Function 1, this function will take a list and return the index positions of any trees.

def tree_position(list):
    trees = []
    for i in range(len(list)):
        if list[i] == -1:
            trees.append(i)
    return trees

# Function 2, this will take a list and return the index positions of any people.

def people_position(list):
    people = []
    for i in range(len(list)):
        if list[i] != -1:
            people.append(i)
    return people

# PEOPLE = [INDEX POSITIONS]

# Function 3, this will take a list, remove all trees and then sort the height of the remaining people

def people_only(list):
    z = list.count(-1)
    for i in range(z):
        list.remove(-1)
    list.sort()
    return(list)

# Function 4, brings it all together. Inserts trees in the tree index positions, and the people in the people
# index positions.


def sortByHeight(a):

    b = [0] * len(a)
    trees = tree_position(a)
    people = people_position(a)
    sorted_people = people_only(a)


    for i in trees:
        b[i] = -1

    for j in range(len(people)):
        for x in range(len(b)):
            if x == people[j]:
                b[x] = sorted_people[j]


    return(b)




print(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))









