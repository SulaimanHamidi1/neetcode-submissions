class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        q = deque()
        indegree = [0] * numCourses
        adjlist = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            indegree[crs] += 1
            adjlist[pre].append(crs)
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        finish = 0
        while q:
            node = q.popleft()
            res.append(node)
            finish += 1
            for dep in adjlist[node]:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    q.append(dep)
        
        if finish == numCourses:
            return res
        
        return []

