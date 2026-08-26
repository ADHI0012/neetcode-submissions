# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(root, path_sum):
            nonlocal total  
            if not root:
                return 0
            if not root.left and not root.right:
                path_sum = path_sum * 10 + root.val
                total += path_sum
            
            dfs(root.left, path_sum * 10 + root.val)
            dfs(root.right, path_sum * 10 + root.val)
        
        dfs(root, 0)
        return total