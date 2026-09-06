class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adj = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        prereq = [set() for _ in range(numCourses)]
        res = []

        for u,v in prerequisites:
            adj[u].append(v)
            indegree[v] += 1

        q = collections.deque()
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            x = q.popleft()


            for j in adj[x]:
                prereq[j].add(x)

                prereq[j].update(prereq[x])

                indegree[j] -= 1

                if indegree[j] == 0:
                    q.append(j)
        
        for u,v in queries:
            if u not in prereq[v]:
                res.append(False)
            else:
                res.append(True)
        
        return res