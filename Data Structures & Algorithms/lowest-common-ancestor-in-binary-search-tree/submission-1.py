# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Go to p and q check if their parents match
        # if yes, return that parent
        # if not, go back once for one node and check again
        # if still no, go back for the second node and check again
        # also check if the parent of node p is the same as q or parent of q and vice versa
        
        parent = {root : None}

        def dfs(root):
            if not root:
                return

            if root.left:
                parent[root.left] = root
                dfs(root.left)
            if root.right:
                parent[root.right] = root
                dfs(root.right)

        dfs(root)
        anc = set()

        while p:
            anc.add(p)
            p = parent[p]

        while q not in anc:
            q = parent[q]
        
        return q

            
            

            

