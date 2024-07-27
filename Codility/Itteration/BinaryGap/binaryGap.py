# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    res =0
    count=0
    tmp =N
    # search through binary bits and shift to the right by 1
    while N:
        # if right most bit & 1 equal to 0 
        # then its not the loongest sequence of 0s
        if N &1 ==0:
            res +=1

        # if the right most bit & 1 equals to 1 then we take compare the length
        # with longest length we measured and shift the bit
        else:
            count = max(count,res)
            res =0
        N =N>>1
    # edge case for when there are no 1s after the frist left most bit
    if count ==len(bin(tmp))-3:
        return 0
    else:
        return count


# 86%


            
