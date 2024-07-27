# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        tmp = []
        dummy = ListNode(-1)
        tail = dummy 
        for i in lists:
            while i:
                tmp.append(i.val)
                i = i.next
                
        tmp.sort()
        for i in tmp:
            tail.next = ListNode(i)
            tail =tail.next
        return dummy.next