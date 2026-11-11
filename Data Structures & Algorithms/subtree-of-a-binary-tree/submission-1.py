# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(root, subTree):
            if not root and not subTree:
                return True
            if root and subTree and root.val == subTree.val:
                return (
                    isSameTree(root.left, subTree.left) and
                    isSameTree(root.right, subTree.right)
                )
                
            return False

        if not root:
            return False
        if not subRoot:
            return True
        if isSameTree(root, subRoot):
            return True
            
        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))   

        
        