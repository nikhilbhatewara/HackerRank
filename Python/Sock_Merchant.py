#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    #pair: number of pairs 
    
    # Sort the array and then start checking if the values match. If they do, increase the counter(pair) and increase the iterator by 2 since the previous values are already counted in the pair
    pair = 0
    arSorted = sorted(ar)
    i=0
    while(i<n-1):
         
        if arSorted[i]==arSorted[i+1]:
            pair=pair+1
            i=i+2
        else:
            i=i+1
    return pair
       
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
