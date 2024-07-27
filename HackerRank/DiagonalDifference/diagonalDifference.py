#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    left = 0
    right = 0
    for i in range(len(arr)):
        left= left +arr[i][i]
    
    i = len(arr) - 1
    j = 0
    while i >= 0 and j < len(arr[0]):
        right =right +arr[i][j]
        i -= 1
        j += 1
    return abs(left-right)
        
            
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
