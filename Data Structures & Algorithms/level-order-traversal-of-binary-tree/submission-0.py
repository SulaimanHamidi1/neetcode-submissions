# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Use dfs to go as deep as possible
        #Use a hashmap with level as key and nodes at the specific level as values
        #increment level with each function call

        nodes = {}
    
        def dfs(root, i):

            if not root:
                return
            
            if i in nodes:
                nodes[i].append(root.val)
            else:
                nodes[i] = [root.val]
            
            dfs(root.left, i + 1)
            dfs(root.right, i + 1)

        dfs(root, 1)
        
        return list(nodes.values())




            

            


        
