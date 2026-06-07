class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prereqs = {i:[] for i in range(numCourses)}

        for pre, crs in prerequisites:
            prereqs[crs].append(pre)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if prereqs[crs] == []:
                return True
            
            visited.add(crs)
            for pre in prereqs[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            prereqs[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True