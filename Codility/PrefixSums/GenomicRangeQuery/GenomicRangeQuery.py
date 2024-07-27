def solution(S, P, Q):
    # Create prefix sums for each nucleotide
    N = len(S)
    A, C, G, T = [0] * (N + 1), [0] * (N + 1), [0] * (N + 1), [0] * (N + 1)

    for i in range(N):
        A[i + 1] = A[i] + (1 if S[i] == 'A' else 0)
        C[i + 1] = C[i] + (1 if S[i] == 'C' else 0)
        G[i + 1] = G[i] + (1 if S[i] == 'G' else 0)
        T[i + 1] = T[i] + (1 if S[i] == 'T' else 0)

    # Process the queries
    result = []
    for i in range(len(P)):
        start, end = P[i], Q[i] + 1
        if A[end] - A[start] > 0:
            result.append(1)
        elif C[end] - C[start] > 0:
            result.append(2)
        elif G[end] - G[start] > 0:
            result.append(3)
        elif T[end] - T[start] > 0:
            result.append(4)

    return result

# Chatgpt
# 100%
