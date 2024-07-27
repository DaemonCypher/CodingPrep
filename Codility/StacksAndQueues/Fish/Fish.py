# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    downstream = []  # Stack to keep the downstream-moving fish
    survivors = 0

    for i in range(len(A)):
        # If the fish is moving downstream, add it to the stack
        if B[i] == 1:
            downstream.append(A[i])
        else:
            # The fish is moving upstream. It will meet the downstream fish.
            while downstream:
                # If the downstream fish is larger, the upstream fish gets eaten
                if downstream[-1] > A[i]:
                    break
                # If the upstream fish is larger, it eats the downstream fish
                else:
                    downstream.pop()

            # If no fish in the stack, the upstream fish survives
            if not downstream:
                survivors += 1

    # Count the remaining downstream fish as survivors
    survivors += len(downstream)

    return survivors
# Chatgpt
# 100%