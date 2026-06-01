# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int):
        def is_there(root, total):
            if not root:
                return False
            if not root.left and not root.right:
                return total + root.val == targetSum
            return (is_there(root.left, root.val + total) or is_there(root.right, total + root.val))


        return is_there(root, 0)