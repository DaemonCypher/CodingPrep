# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # add the values in the list node to a list
        l1TMP = []
        while list1:
            l1TMP.append(list1.val)
            list1 =list1.next

        # add the values in the list node to a list
        l2TMP = []
        while list2:
            l2TMP.append(list2.val)
            list2 =list2.next

        # combined both list into 1
        combined = l1TMP
        combined.extend(l2TMP)

        # sort the list that has value from list1 and list2
        combined.sort()
        dummy = ListNode(-1)
        tail = dummy
        # create a new listNode and add the values from combined
        for i in combined:
            tail.next = ListNode(i)
            tail =tail.next
        return dummy.next