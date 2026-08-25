class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q = collections.deque()
        inorder = [0 for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]
        topo = []

        for u,v in prerequisites:
            adj[u].append(v)
            inorder[v] += 1
        
        for i in range(numCourses):
            if inorder[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            topo.append(node)

            for x in adj[node]:
                inorder[x] -= 1
                if inorder[x] == 0:
                    q.append(x)
        
        return len(topo) == numCourses