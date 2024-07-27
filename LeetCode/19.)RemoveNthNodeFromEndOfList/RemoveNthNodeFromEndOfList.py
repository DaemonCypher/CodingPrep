# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = []
        dummy = head
        res = ListNode()
        cur = res
        while dummy:
            tmp.append(dummy.val)
            dummy = dummy.next
    
        val= tmp.pop(len(tmp)-(n))
        for i in tmp:
            cur.next = ListNode(i)
            cur = cur.next
            
        return res.next