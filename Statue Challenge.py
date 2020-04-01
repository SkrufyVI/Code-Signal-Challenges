'''

Bob got statues of different sizes as a present from Adam for his birthday.
Each statue has a non-negative integer size.
Since he likes to make things perfect, he wants to arrange them from smallest to largest.
Each statue will be bigger than the previous one exactly by 1.
He may need some additional statues to accomplish that.
Help him figure out the minimum number of additional statues needed.

E.g.
For statues = [6, 2, 3, 8];
The output should be 3 because Bob needs statues of sizes 4,5 and 7.

'''



def makeArrayConsecutive2(statues):
    statues.sort()
    length = len(statues)
    extra_statues = 0
    for i in range(0, length - 1):
        if statues[i+1] != statues[i] + 1:
            if (statues[i+1]) - (statues[i]+1) == -1:
                extra_statues += 0
            else:
                extra_statues += (statues[i+1]) - (statues[i] + 1)

    return extra_statues






