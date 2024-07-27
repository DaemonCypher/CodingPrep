def solution(A):
    min_avg_value = float('inf')
    min_avg_pos = 0

    for i in range(0, len(A)-2):
        # Check the average of the slice with 2 elements
        avg_2 = (A[i] + A[i + 1]) / 2.0
        if avg_2 < min_avg_value:
            min_avg_value = avg_2
            min_avg_pos = i
        
        # Check the average of the slice with 3 elements
        avg_3 = (A[i] + A[i + 1] + A[i + 2]) / 3.0
        if avg_3 < min_avg_value:
            min_avg_value = avg_3
            min_avg_pos = i

    # Check the last two elements
    if (A[-2] + A[-1]) / 2.0 < min_avg_value:
        min_avg_pos = len(A) - 2

    return min_avg_pos

# ChatGpt
# 100%
