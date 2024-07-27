# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    l,r = 0,1
    profit =0
    while r<len(A):
        if A[l] < A[r]:
            profit = max(A[r]-A[l],profit)
        else:
            l=r
        r+=1
    return profit
# 100%