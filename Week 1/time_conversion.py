#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

def timeConversion(s):
    if s[8] == 'A':
        if int(s[0:2]) == 12:
            new_s = '00' + s[2:8]
            return (new_s)
        else:
            return s[0:8]
    elif s[8] == 'P':
        if int(s[0:2]) == 12:
            return s[0:8]
        else:
            hh_24hr = int(s[0:2]) + 12
            new_s = str(hh_24hr) + s[2:8]
            return(new_s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
