class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q = collections.deque()
        indegree = [0 for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]
        topo = []

        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            topo.append(node)

            for x in adj[node]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    q.append(x)
        
        if len(topo) == numCourses:
            return topo
        
        return []
