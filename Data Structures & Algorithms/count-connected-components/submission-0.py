class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjlist = {i: [] for i in range(n)}
        for src, dst in edges:
            adjlist[src].append(dst)
            adjlist[dst].append(src)
        
        seen = set()

        def dfs(node):
            if node in seen:
                return
            
            seen.add(node)
            for nei in adjlist[node]:
                dfs(nei)
        
        count = 0
        for i in range(n):
            if i in seen:
                continue
            count += 1
            dfs(i)

        return count



