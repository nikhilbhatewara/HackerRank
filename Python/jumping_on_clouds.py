#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps, i = 0, 0
    while i < len(c)-1:
        print("Index Number ",i)
        # if 2 cloud jumps
        if i+2 < len(c) and c[i+2] != 1:
            print("2 jumps")
            i += 1
        
        jumps =jumps + 1
        
        i =i + 1
     
    return jumps
            
            

    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
