def solution(N, A):
    counters = [0] * N
    current_max = 0
    last_update = 0

    for operation in A:
        if 1 <= operation <= N:
            # Apply lazy update
            if counters[operation - 1] < last_update:
                counters[operation - 1] = last_update

            # Increase the counter
            counters[operation - 1] += 1

            # Update current_max if necessary
            if counters[operation - 1] > current_max:
                current_max = counters[operation - 1]
        else:
            # Update last_update for max counter operation
            last_update = current_max

    # Apply the lazy updates to all counters
    for i in range(N):
        if counters[i] < last_update:
            counters[i] = last_update

    return counters