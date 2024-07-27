def solution(N, A):
    res = [0] * N
    for i in A:
        if i == (N + 1):
            max_val = max(res)
            res = [max_val] * N  # Set all elements to the max value
        else:
            res[i - 1] += 1  # Increment the (i-1)th element
    return res


# 66% score