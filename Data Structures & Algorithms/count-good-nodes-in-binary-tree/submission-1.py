# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0

        def dfs(root, cur_max):
            nonlocal cnt

            if not root:
                return
            
            if root.val >= cur_max:
                cnt += 1
            
            cur_max = max(root.val, cur_max)

            dfs(root.left, cur_max)
            dfs(root.right, cur_max)
        
        dfs(root, root.val)
        return cnt
        



        
            