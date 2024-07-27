#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def bubbleSort(arr):
     
    n = len(arr)
 
    # For loop to traverse through all
    # element in an array
    for i in range(n):
        for j in range(0, n - i - 1):
             
            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found
            #is greater than the adjacent element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
def miniMaxSum(arr):

    bubbleSort(arr)
    small =0
    large = 0
    for i in range(1,len(arr),1):
        large=large+arr[i]
    for i in range(0,len(arr)-1,1):
        small=small+arr[i]
        
    print(small,large)
        
    # Write your code here

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
