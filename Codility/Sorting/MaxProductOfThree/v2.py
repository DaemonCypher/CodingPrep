# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A.sort()
    tmp = A[0]* A[1]
    length = len(A)-1
    res = 0
    if tmp >=0:
        res = tmp * A[length]
    last = A[length] * A[length-1] * A[length-2]
    res = max(last,res)
    return res


# 100%