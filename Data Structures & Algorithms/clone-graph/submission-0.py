"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        look_up = {}
        def dfs(node):
            if node in look_up:
                return look_up[node]
            
            copy = Node(node.val)
            look_up[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        
        if not node:
            return None
        
        return dfs(node)
            
