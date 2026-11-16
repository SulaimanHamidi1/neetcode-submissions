class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q = deque()
        indegree = [0] * numCourses
        adjlist = defaultdict(list)

        for crs, pre in prerequisites:
            indegree[crs] += 1
            adjlist[pre].append(crs)
        
        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)

        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for dep in adjlist[node]:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    q.append(dep)
        
        return finish == numCourses


