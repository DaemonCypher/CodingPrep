# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root):
            result = []

            if root is None:
                return
            # queue = all the nodes at the current level
            queue = [root]
            level = []

            while len(queue) > 0:

                cur_node = queue.pop(0)
                level.append(cur_node.val)
                # when queue size is 0 then all the nodes at the current level are visited
                if len(queue)==0:
                    new = []
                    # format the anwser i.e. all nodes in the current level in a list
                    for i in range(len(level)):
                        new.append(level[i])

                    # add to the current result and reset everything
                    result.append(new)
                    level.clear()

                if cur_node.left is not None:
                    queue.append(cur_node.left)
                if cur_node.right is not None:
                    queue.append(cur_node.right)
            return result

        return (bfs(root))