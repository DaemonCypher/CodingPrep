# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    count = 0
    for i in range(len(A)):
        if A[i] == 0 :
            for j in range(i,len(A),1):
                if A[j] == 0:
                    continue
                else:
                    count +=1
    if count>= 1000000000:
        return -1
    return count
    # 50%