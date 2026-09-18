# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {}
        preIndex = 0
        for index, value in enumerate(inorder):
            indices[value] = index
        def build(l,r):
            if l > r:
                return None
            nonlocal preIndex
            root = TreeNode(preorder[preIndex])
            mid = indices[preorder[preIndex]]
            preIndex += 1

            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)
            return root
        
        return build(0,len(inorder) - 1)