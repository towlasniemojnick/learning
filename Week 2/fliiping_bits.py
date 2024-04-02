#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    num = bin(n)
    num = (34 - len(num)) * '0' + num[2:]
    flipped_num = ''
    for b in num:
        if b == '0':
            flipped_num = flipped_num + '1'
        elif b == '1':
            flipped_num = flipped_num + '0'

    flipped_dec = int(flipped_num,2)

    return flipped_dec

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
