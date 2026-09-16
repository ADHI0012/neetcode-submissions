# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        seen = set()
        def dfs(root1, root2):
            if not root1 or not root2:
                return
            if root1 and root2:
                if root2 not in seen:
                    root1.val += root2.val
                seen.add(root2)
            if not root1.left and root2 and root2.left:
                if root2.left not in seen:
                    root1.left = TreeNode(root2.left.val)
                seen.add(root2.left)
            if not root1.right and root2 and root2.right:
                if root2.right not in seen:
                    root1.right = TreeNode(root2.right.val)
                seen.add(root2.right)
            
            dfs(root1.left, root2.left)
            dfs(root1.right, root2.right)

        if not root1 and root2:
            root1 = root2
            return root1
        
        dfs(root1, root2)
        return root1