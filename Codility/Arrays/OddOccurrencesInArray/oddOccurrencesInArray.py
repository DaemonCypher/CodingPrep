# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    pairs = {} # value: count
    # create a hashmap with values in A and the number of the same values 
    for i in A:
        if i not in pairs:
            pairs[i] = 1
        else:
            pairs[i]+=1

    # search through the hashmap and find the count that is not divisible by 2
    for key, value in pairs.items():
        if value %2 !=0:
            return key
        
    # 100%
