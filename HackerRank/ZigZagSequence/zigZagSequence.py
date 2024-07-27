def findZigZagSequence(a, n):
    a.sort()
    mid = int((n - 1)/2)  # Adjusted to correctly find the middle element
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2  # Adjusted to start the reverse process from the correct position
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1  # Decrement 'ed' to correctly create the zig zag pattern

    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return
