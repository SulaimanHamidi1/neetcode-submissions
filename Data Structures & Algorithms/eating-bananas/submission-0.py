class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        res = r

        while l <= r:
            total = 0
            k = l + (r - l) // 2
            
            for pile in piles:
                total += math.ceil(pile / k)
            if total <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res

        