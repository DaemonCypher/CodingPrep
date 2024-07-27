# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        check = -1000
        res = []
        while head:
            if head.val != check:
                check = head.val
                res.append(check) 
            head = head.next
        dummy=ListNode(0)
        tail = dummy
        for i in res:
            tail.next = ListNode(i)
            tail= tail.next

        return dummy.next