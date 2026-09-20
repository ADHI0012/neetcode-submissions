# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def preorder_traversal(root): # Root Left Right
            nonlocal res
            if not root:
                res.append("#")
                return
            res.append(str(root.val))
            preorder_traversal(root.left)
            preorder_traversal(root.right)
        
        preorder_traversal(root)
        
        return ",".join(res)
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = data.split(",")
        self.index = 0

        def dfs():
            if preorder[self.index] == "#":
                self.index += 1
                return None
            root = TreeNode(preorder[self.index])
            self.index += 1
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()