class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        seen = set()
        adjlist = defaultdict(list)
        
        def dfs(node, prev):
            if node in seen:
                return True
            
            seen.add(node)
            for nei in adjlist[node]:
                if nei == prev:
                    continue
                if dfs(nei, node):
                    return True
            seen.remove(node)
            return False
            
        for src, dst in edges:
            adjlist[src].append(dst)
            adjlist[dst].append(src)

            if dfs(src, -1):
                return [src, dst]

        return []
            
