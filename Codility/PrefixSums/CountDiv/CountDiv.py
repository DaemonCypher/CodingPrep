def solution(A, B, K):
    # Find the first number greater than or equal to A that is divisible by K
    first_multiple = A if A % K == 0 else A + (K - A % K)

    # If the first multiple is greater than B, there are no divisible numbers
    if first_multiple > B:
        return 0

    # Calculate the number of divisible numbers between first_multiple and B
    return (B - first_multiple) // K + 1

# 100%
# ChatGPT