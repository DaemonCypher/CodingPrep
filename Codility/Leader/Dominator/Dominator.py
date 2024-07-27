# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    freq = {}
    for i in A:
        if i not in freq:
            freq.update({i:1})
        else:
            freq[i]+=1
    large = max(freq.values())
    Keymax = max(zip(freq.values(), freq.keys()))[1]

    if large > len(A)//2:
        for i in range(len(A)):
            if A[i] == Keymax:
                return i
    else:
        return -1


def solution(A):
    freq = {}
    for i in A:
        if i not in freq:
            freq.update({i:1})
        else:
            freq[i]+=1
    large = max(freq.values())
    Keymax = max(zip(freq.values(), freq.keys()))[1]

    if large > len(A)//2:
        for i in range(len(A)):
            if A[i] == Keymax:
                return i
    else:
        return -1

# 91%