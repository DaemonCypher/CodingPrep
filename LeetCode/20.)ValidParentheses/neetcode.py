class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedToOpen = { ")" : "(", "]":"[", "}": "{"}

        for i in s:
            if i in closedToOpen:
                if stack and stack[-1] == closedToOpen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        if not stack:
            return True
        else:
            return False