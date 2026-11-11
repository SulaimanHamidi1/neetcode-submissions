class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        q = deque()

        def addcell(r, c):
            if ((r, c) in seen or min(r, c) < 0 or 
                r == rows or c == cols or grid[r][c] == -1):
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
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addcell(r + 1, c)
                addcell(r - 1, c)
                addcell(r, c + 1)
                addcell(r, c - 1)
            dist += 1
        