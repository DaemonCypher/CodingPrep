def solution(A):
    A.sort()  # Sort the array
    for i in range(len(A) - 2):
        # Check if the triplet (A[i], A[i+1], A[i+2]) forms a triangle
        if A[i] + A[i + 1] > A[i + 2]:
            return 1
    return 0

# Chatgpt
# 100%