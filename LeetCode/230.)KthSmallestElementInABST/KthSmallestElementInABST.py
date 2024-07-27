# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorderTraversal(root):
            if root is None:
                return []
            path = []
            path.extend(inorderTraversal(root.left))  # Traverse the left subtree and add to the path
            path.append(root.val)  # Add the current node's value to the path
            path.extend(inorderTraversal(root.right))  # Traverse the right subtree and add to the path
            return path

        path=inorderTraversal(root)
        return path[k-1]