# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root, count):
            if root is None:
                return 0
            leftheight, rightheight = helper(root.left, count+1), helper(root.right, count+1)
            if root.left is None and root.right is None:
                return 1
            if root.left is None:
                return 1 + rightheight
            if root.right is None:
                return 1 + leftheight

            
            return min(leftheight, rightheight) + 1

        return helper(root,0)
    


        