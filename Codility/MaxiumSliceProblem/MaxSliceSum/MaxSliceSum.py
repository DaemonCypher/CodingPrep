# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    maxSub = A[0]
    cursum = 0
    for n in A:
        if cursum < 0:
            cursum = 0
        cursum += n
        maxSub = max (maxSub, cursum)
    return maxSub