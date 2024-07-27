# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math
def solution(X, Y, D):
    value = Y-X

    if value ==0:
        return 0

    return math.ceil(value/D)

# 100%