class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
            Since x2 and y2 are always 0 we can simplify the sqrt((x1 - x2)^2 + (y1 - y2)^2)
            formula to x*x + y*y
        """

        heap = []
        for x, y in points:
            heapq.heappush(heap, (-(x*x + y*y), x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [[x, y] for _, x, y in heap]