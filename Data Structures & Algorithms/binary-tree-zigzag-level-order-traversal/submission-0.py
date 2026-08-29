# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        res = []
        def zigzag_level_order(root):
            q.append(root)
            k = 0

            while q:
                size = len(q)
                r = []
                for _ in range(size):
                    node = q.popleft()
                    r.append(node.val)

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                if not k % 2:
                    res.append(r)
                else:
                    res.append(r[::-1])
                k += 1

        if not root:
            return res
        
        zigzag_level_order(root)
        return res
        
        
