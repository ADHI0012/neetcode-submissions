class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        def hasPath(source, dest):
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
        
        for u,v in edges:
            if hasPath(u,v):
                return [u,v]
            adj[u].append(v)
            adj[v].append(u)
            
