# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            return 1 + max(left, right)

        if not root:
            return 0
        left = height(root.left)
        right = height(root.right)
        return max(left + right, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        