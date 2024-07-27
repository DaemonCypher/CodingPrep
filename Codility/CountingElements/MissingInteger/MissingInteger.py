# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    A.sort()

    check =1 
    for i in A:
        if i == check:
            check +=1
        if i>check:
            break
    return check