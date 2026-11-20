class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        floors = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            floors[i] = min(floors[i-1] + cost[i-1],
                            floors[i-2] + cost[i-2])

        return floors[len(cost)]
