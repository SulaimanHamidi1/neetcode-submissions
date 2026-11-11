class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh_cnt = 0

        def makeRot(r, c):
            nonlocal fresh_cnt
            if (
                min(r, c) < 0 or r >= rows or c >= cols or
                grid[r][c] == 0 or grid[r][c] == 2
            ):
                return
        
            grid[r][c] = 2
            q.append([r, c])
            fresh_cnt -= 1
                   
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    fresh_cnt += 1

        res = 0
        while q:
            temp = fresh_cnt
            q_len = len(q)
            for i in range(q_len):
                r, c = q.popleft()
                makeRot(r+1, c)
                makeRot(r-1, c)
                makeRot(r, c+1)
                makeRot(r, c-1)
            if temp != fresh_cnt:
                res += 1
        
        return -1 if fresh_cnt != 0 else res
            
            