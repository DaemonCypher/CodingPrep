# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    """
    :param A: a list of integers
    :return: true if the list is a permutation (sequence from 1 to N)

    One-by-one, add each value to a set.
        Abort if the value is not valid for the permutation
        Abort if the value is a duplicate
    It is a permutation.
    """
    if not len(A):
        return 0  # An empty list is not a permutation.
    collection = set()
    length = 0
    for item in A:
        if item > len(A):
            return 0  # Item is too big for the permutation.
        collection.add(item)
        length += 1
        if len(collection) != length:
            return 0  # Length of set did not increase, so item is a duplicate.
    return 1