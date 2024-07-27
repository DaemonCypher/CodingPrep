# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a temporay list to store listNode values
        temp = []
        # itterate through the listNode and append values to temp
        while head:
            temp.append(head.val)
            head = head.next
        # initialize a new listNode to be returned
        dummy = ListNode(0)
        tail = dummy
        # reverse the list so 1, 2, 3, 4 == 4, 3, 2, 1
        temp.reverse()

        # add the values from temp list to new listNode
        for i in temp:
            tail.next = ListNode(i)
            tail= tail.next
        return dummy.next
            