# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        left = ""
        # convert and append all values of linked list to a string
        while head:
            value = head.val
            left = left+str(value)
            head= head.next

        # reverse string and check if left and right equal
        right = left[::-1]

        if left == right:
            return True
        else:
            return False
