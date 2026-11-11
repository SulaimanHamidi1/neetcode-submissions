"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        new = {}

        def clone(cur):
            if cur in new:
                return new[cur]
            
            copy = Node(cur.val)
            new[cur] = copy
            for nei in cur.neighbors:
                copy.neighbors.append(clone(nei))
            return copy
        
        return clone(node) if node else None