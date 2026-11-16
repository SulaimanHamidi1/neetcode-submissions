class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjdict = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adjdict[crs].append(pre)

        seen = set()

        def dfs(crs):
            if crs in seen:
                return False
            
            if adjdict[crs] == []:
                return True
            
            seen.add(crs)
            for pre in adjdict[crs]:
                if not dfs(pre):
                    return False
            seen.remove(crs)
            adjdict[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True

