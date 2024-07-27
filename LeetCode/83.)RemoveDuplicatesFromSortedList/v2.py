# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        check = -1000
        dummy=ListNode(0)
        tail = dummy
        while head:
            if head.val != check:
                check = head.val
                tail.next = ListNode(check)
                tail= tail.next
            head = head.next

        return dummy.next