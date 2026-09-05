class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adj = [[] for _ in range(numCourses)]
        res = []

        for u,v in prerequisites:
            adj[u].append(v)
        
        def bfs(source, dest):
            q = collections.deque()
            visited = set()
            q.append(source)
            visited.add(source)

            while q:
                x = q.popleft()
                if x == dest:
                    return True

                for j in adj[x]:
                    if j not in visited:
                        q.append(j)
                        visited.add(j)
            return False
        
        for u,v in queries:
            res.append(bfs(u,v))
        
        return res
        
