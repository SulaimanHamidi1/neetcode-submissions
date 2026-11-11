class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r >= rows or c >= cols or r < 0 or c < 0:
                return
            
            if grid[r][c] == '0' or (r, c) in seen:
                return
            
            seen.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in seen:
                    dfs(r, c)
                    count += 1
        
        return count
            
        