# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        lst = []
        def dfs(root, lvl):
            if not root:
                return
            
            if len(lst) == lvl:
                lst.append([])
            lst[lvl].append(root.val)
            
            dfs(root.left, lvl + 1)
            dfs(root.right, lvl + 1)
        
        dfs(root, 0)
        res = []

        for nodes in lst:
            res.append(nodes[-1])
        
        return res



