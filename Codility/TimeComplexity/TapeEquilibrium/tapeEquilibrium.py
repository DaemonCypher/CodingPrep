# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    res = float('inf')
    for i in range(len(A)):
        first = sum(A[:i+1])
        sec = sum(A[i+1:])
     
        total = abs(first - sec)

        res = min(res,total)
    
        
    # Implement your solution here
    return res

# 38% score
