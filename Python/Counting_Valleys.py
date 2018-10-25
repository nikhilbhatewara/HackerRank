#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    # level: track the elevation from sea level
    # Valley: Counter for valley
    level = 0
    valley = 0
    for i in range(0,len(s)):
        # For every U, increase the level
        if s[i]== 'U':
            level= level + 1
            # Check if after taking a step up the hiker has reached the sea level. If yes, he came up from valley
            if (level == 0):
                valley=valley+1
    
        else:
             level =level - 1
            
        
    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
