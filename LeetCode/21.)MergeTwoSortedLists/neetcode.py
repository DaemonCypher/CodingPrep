# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        tail = merged
    
        # if both list are not null or we have not reached the end of one list
        while list1 and list2:
            # find which value in the list node is the smallest
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # if a list empty append the rest to tail
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return merged.next
            
