# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        arrp = []
        arrq = []

        if not p and not q:
            return True

        def dfs(root, arr):
            if not root:
                arr.append(root)
                return root
            dfs(root.left, arr)
            dfs(root.right, arr)
            arr.append(root)
            
        
        dfs(p, arrp)
        dfs(q, arrq)

        if len(arrp) != len(arrq):
            return False
        
        for i in range(len(arrp)):
            
            if not arrp[i] and not arrq[i]:
                continue
            if not arrp[i] or not arrq[i]:
                return False
            if arrp[i].val != arrq[i].val:
                return False
        
        return True

        


            


        
        


