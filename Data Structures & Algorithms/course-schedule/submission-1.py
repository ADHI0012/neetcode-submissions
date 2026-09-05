class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        inorder = [0 for _ in range(numCourses)]
        topo = []

        for u,v in prerequisites:
            adj[v].append(u)
            inorder[u] += 1
        
        q = collections.deque()

        for i in range(numCourses):
            if inorder[i] == 0:
                q.append(i)

        while q:
            x = q.popleft()
            topo.append(x)

            for j in adj[x]:
                    inorder[j] -= 1
                    if inorder[j] == 0:
                        q.append(j)

        return len(topo) == numCourses
        


