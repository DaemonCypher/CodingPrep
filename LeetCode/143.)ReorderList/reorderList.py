# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        tmp = []
        dummy = head
        while dummy:
            tmp.append(dummy.val)
            dummy = dummy.next

        tmp.reverse()
        count = 0
        res = ListNode()
        cur = res
    
        for i in range(len(tmp)):
            if i %2 ==0:
                cur.next = ListNode(head.val)
                cur = cur.next
                head= head.next
            else:
                cur.next = ListNode(tmp[count])
                cur = cur.next
                count+=1
        #return res.next
        # incomplete soultion cant get Leet code to see res as the anwser
        


