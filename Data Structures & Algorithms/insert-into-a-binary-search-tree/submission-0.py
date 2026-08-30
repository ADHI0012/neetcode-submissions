# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return
            if val < root.val:
                if not root.left:
                    root.left = TreeNode(val)
                    return
                else:
                    dfs(root.left)
            else:
                if not root.right:
                    root.right = TreeNode(val)
                    return
                else:
                    dfs(root.right)

        if not root:
            root = TreeNode(val)
            return root
        
        dfs(root)
        return root