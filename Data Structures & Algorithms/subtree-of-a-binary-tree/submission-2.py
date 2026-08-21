# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(root1, root2):
            print("getting called")
            if not root1 and not root2:
                return True
            if not root1 and root2:
                return False
            if root1 and not root2:
                return False
            if root1 and root2 and root1.val != root2.val:
                return False

            return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)

        
        def dfs(root1, root2):
            if root1 and root2 and root1.val == root2.val:
                if isSameTree(root1, root2):
                    return True
            if not root1 or not root2:
                return False
            return dfs(root1.left, root2) or dfs(root1.right, root2)
        

        return dfs(root, subRoot)

