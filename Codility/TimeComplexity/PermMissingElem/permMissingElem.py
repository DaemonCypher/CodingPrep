# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    value = []
    for i in range(1,len(A)+2):
        value.append(i)

    return sum(value) - sum(A)