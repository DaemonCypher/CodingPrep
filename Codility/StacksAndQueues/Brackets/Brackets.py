# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    stack = []
    closedToOpen = { ")" : "(", "]":"[", "}": "{"}

    for i in S:
        if i in closedToOpen:
            if stack and stack[-1] == closedToOpen[i]:
                stack.pop()
            else:
                return 0
        else:
            stack.append(i)

    if not stack:
        return 1
    else:
        return 0
    
# 100%