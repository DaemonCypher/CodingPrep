def solution(A):
    # Step 1: Find the leader of the array, if it exists
    size = 0
    value = None
    for elem in A:
        if size == 0:
            size += 1
            value = elem
        else:
            if elem != value:
                size -= 1
            else:
                size += 1
    
    candidate = -1
    if size > 0:
        candidate = value
    
    leader_count = A.count(candidate)
    
    # Step 2: Check for equi leaders
    equi_leaders = 0
    left_count = 0
    for i in range(len(A)):
        if A[i] == candidate:
            left_count += 1
        if left_count > (i + 1) // 2 and leader_count - left_count > (len(A) - i - 1) // 2:
            equi_leaders += 1

    return equi_leaders

# Chatgpt
# 100%
