class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        rows = len(grid)
        cols = len(grid[0])

        count = [0]
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if (r, c) in seen or grid[r][c] == 0:
                return
            
            count[0] += 1
            seen.add((r, c))
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0 and (r, c) not in seen:
                    dfs(r, c)
                    maxArea = max(maxArea, count[0])
                    count[0] = 0

        return maxArea