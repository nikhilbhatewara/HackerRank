#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    # Length of Input
    l=len(s)
    # Number of time we can append
    i=n//l
    print(i)
    #the reminder will decide the last string   
    r=n % l
    print(r)
    count=s.count('a') * i + s[0:r].count('a')
    
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
