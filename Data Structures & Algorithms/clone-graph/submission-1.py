"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        look_up = {}
        q = collections.deque()

        def bfs(node):
            q.append(node)
            look_up[node] = Node(node.val)
            while q:
                n = q.popleft()
                copy = look_up[n]
                for nei in n.neighbors:
                    if nei not in look_up:
                        look_up[nei] = Node(nei.val)
                        q.append(nei)
                    copy.neighbors.append(look_up[nei])
            return look_up[node]


        if not node:
            return None

        return bfs(node)
