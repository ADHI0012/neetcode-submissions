class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        

        def hasPath(source, destination):
            q = collections.deque([source])
            visited = set()
            visited.add(source)

            while q:
                x = q.popleft()

                for j in adj[x]:
                    if j not in visited:
                        q.append(j)
                        visited.add(j)
            
            return destination in visited


        
        for u,v in edges:
            if hasPath(u,v):
                return [u,v]
            adj[u].append(v)
            adj[v].append(u)
