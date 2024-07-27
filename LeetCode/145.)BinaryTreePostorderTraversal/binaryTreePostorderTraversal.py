# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root,res):
            if root:

                helper(root.left,res)
                helper(root.right,res)
                res.append(root.val)

        res =[]
        res.append(helper(root,res))
        # post process clean up for Null/None that is added to the list
        res = [ele for ele in res if ele != None]
        return res