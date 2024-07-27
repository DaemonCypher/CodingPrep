# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        tmp = head
        while tmp:
            if tmp in visited:
                return True
            else:
                visited[tmp] = True
            tmp = tmp.next
        return False