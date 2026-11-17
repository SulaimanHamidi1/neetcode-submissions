class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False
        
        visited = set()
        adjlist = {node: [] for node in range(n)}

        for src, dst in edges:
            adjlist[src].append(dst)
            adjlist[dst].append(src)
        
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for nei in adjlist[node]:
                dfs(nei)
        
        dfs(0)
        return len(visited) == n
            
