def solution(A):
    total_sum = sum(A)
    min_diff = float('inf')
    left_sum = 0

    for i in range(len(A) - 1):  # Iterate till the second last element
        left_sum += A[i]
        right_sum = total_sum - left_sum
        diff = abs(left_sum - right_sum)
        min_diff = min(min_diff, diff)

    return min_diff

# 100% score
