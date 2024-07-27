# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3=ListNode(0)
        l3tmp=l3
        l1Num=""
        l2Num=""
        # create two empty strings to itterate through the list and append values in order
        while l1 != None:
            tmp1=l1.val
            l1Num= str(tmp1)+l1Num
            l1=l1.next
        while l2 != None:
            tmp2=l2.val
            l2Num= str(tmp2)+l2Num
            l2=l2.next
        # convert the strings back to int and add them together
        l1Num=int(l1Num)
        l2Num=int(l2Num)
        tmp =l1Num +l2Num
        # convert the int back to a string to access individual values
        tmp=str(tmp)
        # itterate through the string and create a new list node to return
        for i in range(len(tmp)-1,-1,-1):
            newNode=ListNode(tmp[i])
            l3tmp.next=newNode
            l3tmp=newNode
        return l3.next