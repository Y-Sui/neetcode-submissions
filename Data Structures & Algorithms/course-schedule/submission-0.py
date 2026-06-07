class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """

        拓扑排序 (Topological Sort) 的简化版。

简单来说，这道题就是问你：这个有向图中是否存在环 (Cycle)？ 有环就死锁了

DFS 检测环
"""
        # key: 前置课程 (pre), value: 后续课程列表 (list of next courses)
        preMap = { i:[] for i in range(numCourses) }
        for crs, pre in prerequisites:
            preMap[pre].append(crs)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False

            if preMap[crs] == []:
                return True

            visited.add(crs)

            # 3. 递归检查所有的后续课程
            for next_crs in preMap[crs]:
                if not dfs(next_crs):
                    return False

            # 4. 回溯：把当前课程从“正在访问”中移除
            visited.remove(crs)

            preMap[crs] = []
            
            return True

        # 6. 因为图可能是不连通的（有很多个独立的课），所以要遍历所有课程
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True