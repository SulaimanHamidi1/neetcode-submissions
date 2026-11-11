class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        q = deque()

        fresh_cnt = 0

        def rotten(r, c):
            nonlocal fresh_cnt
            if (
                (r, c) in seen or min(r, c) < 0 or
                r >= rows or c >= cols or grid[r][c] == 0
            ):
                return
            
            fresh_cnt -= 1
            seen.add((r, c))
            q.append([r, c])

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                    seen.add((r, c))
                if grid[r][c] == 1:
                    fresh_cnt += 1
        
        res = 0
        while q:
            len_q = len(q)
            temp = fresh_cnt
            for i in range(len_q):
                
                r, c = q.popleft()
                grid[r][c] = 2
                rotten(r+1, c)
                rotten(r-1, c)
                rotten(r, c+1)
                rotten(r, c-1)
                
            if temp != fresh_cnt:
                res += 1
            
        return -1 if fresh_cnt > 0 else res
            