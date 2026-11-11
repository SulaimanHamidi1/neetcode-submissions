class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        q = deque()

        def addcell(r, c):
            if (min(r, c) < 0 or (r, c) in seen or
                    r >= rows or c >= cols or grid[r][c] == -1
                ):
                return

            seen.add((r, c))
            q.append([r, c])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    seen.add((r, c))
                    q.append([r, c])
        
        dist = 0
        while q:
            q_len = len(q)
            for i in range(q_len):
                r, c = q.popleft()
                grid[r][c] = dist
                addcell(r+1, c)
                addcell(r-1, c)
                addcell(r, c+1)
                addcell(r, c-1)
            dist += 1

        