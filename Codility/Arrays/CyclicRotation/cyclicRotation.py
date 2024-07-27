# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # Implement your solution here
    first = []
    second = []
    value = len(A)-K

    for i in range(len(A)):
        if i < value:
            first.append(A[i])
        else:
            second.append(A[i])
    for i in first:
        second.append(i)
    return second
