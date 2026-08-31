# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        res = []

        def level_order(root):
            q.append(root)

            while q:
                size = len(q)
                for i in range(size):
                    node = q.popleft()
                    if i == size - 1:
                        res.append(node.val)
                    
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        
        if not root:
            return res
        
        level_order(root)
        return res
