'''
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

'''

#First solution below. This function removes a single element from the list, then checks if the sequence is strictly increasing, then re-inserts the element it removed.


# Lesson 1, counter = 0 had to be placed INSIDE the loop as it would set itself to 1 for one flawed run through but save itself as higher than 1
# Lesson 2, I had to use a While Loop to get out of index error of FOR loop. Should remember this for future attempts to dynamically alter lists.
# Lesson 3, counter += 1 for an error, counter += 0 for perfection. Perfection, therefore, means every loop was perfect, as it tests for counter == 0



def almostIncreasingSequence(sequence):
    length = len(sequence)
    i = 0
    while length > i:
        counter = 0

        num = sequence[i]
        sequence.pop(i) #Delete element from list -> check whether list is strictly increasing, repeat (sequence.insert) below.

        if len(sequence) == 1:
            answer = True
            break

        for number in range(len(sequence)-1):
            if sequence[number] >= sequence[number + 1]:
                counter += 1
            else:
                counter += 0

        sequence.insert(i, num)
        i += 1

        if counter == 0:
            answer = True
            break
        else:
            answer = False
    return(answer)

# Problem with the above is it is exceptionally slow and clunky. It takes ages when the list in question has thousands of elements.
# Need to find a cleaner method.

# Step 1, Return the first index of a pair of elements where the earlier element is not less than the later elements
# If no such pair exists, return -1:


def first_bad_pair(sequence):
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return i #This returns the INDEX position of the first element in the bad pair.
    return -1

# Use the above function to make our second one.
# Return whether it is possible to obtain a strictly increaisng sequence by removing NO MORE than one element from the array.


def almostIncreasingSequence(sequence):

    j = first_bad_pair(sequence)

    if j == -1:
        return True  # List is increasing already, all good!

    if first_bad_pair(sequence[j-1:j] + sequence[j+1:]) == -1:
        return True  # Deleting earlier element makes increasing

    if first_bad_pair(sequence[j:j+1] + sequence[j+2:]) == -1:
        return True  # Deleting later element makes increasing

    return False  # Deleting either does not make increasing

# This one is more efficient so passes the Code Signal time test.
# The key lesson from above was that  that "+" means concatenation for lists.
