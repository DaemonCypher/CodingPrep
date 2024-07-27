# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # Implement your solution here
    leaves = set()
    for count, leaf in enumerate(A):
        if leaf <= X:   # Only collect the leaves we need to get to X.
            leaves.add(leaf)
            if len(leaves) >= X:
                return count
    return -1