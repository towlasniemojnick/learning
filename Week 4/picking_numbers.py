#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
a = []
a.reverse();
def pickingNumbers(a):
    # Write your code here
    counts_array = []
    numbers = []
    arrays = []
    counter = 1

    a.sort()
    print(a)
    for i in range(0,len(a)-1):
        if a[i+1] - a[i] <= 1:
            print(a[i+1])
            counter = counter+1
        else:
            counts_array.append(counter)
            counter = 1

    print(counts_array)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()



