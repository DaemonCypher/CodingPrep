# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Perform level order traversal on a binary tree.

        Args:
        root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
        List[List[int]]: A list of lists, where each inner list contains the values
                        of the nodes at that level in the binary tree.
        """

        # If the tree is empty (root is None), return an empty list.
        if root is None:
            return []

        # This list will hold the final result, where each element is a list of node values at each level.
        result = []

        # Initialize a queue with the root node to start the level order traversal.
        queue = [root]

        # Continue the loop as long as there are nodes in the queue.
        while queue:
            # Determine the number of nodes at the current level.
            level_size = len(queue)

            # This list will hold the node values for the current level.
            level = []

            # Iterate over all nodes at the current level.
            for _ in range(level_size):
                # Pop the first node from the queue.
                node = queue.pop(0)

                # Add the node's value to the current level's list.
                level.append(node.val)

                # If the node has a left child, add it to the queue for the next level.
                if node.left:
                    queue.append(node.left)

                # Similarly, if the node has a right child, add it to the queue.
                if node.right:
                    queue.append(node.right)

            # After processing all nodes at this level, add the level list to the result.
            result.append(level)

        return result
