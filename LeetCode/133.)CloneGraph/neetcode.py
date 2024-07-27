"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old = {}

        def dfs(node):
            if node in old:
                return old[node]
    
            copy = Node(node.val)
            old[node] = copy

            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        if node:
            return dfs(node) 
        else:
            return None