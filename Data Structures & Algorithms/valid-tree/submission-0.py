class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hasCycle = False
        components = 0
        visited = set()
        if len(edges) != n - 1:
            return False
        
        adj = [[] for _ in range(n + 1)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def bfs(source):
            nonlocal hasCycle
            q = collections.deque()
            q.append((source,-1))
            visited.add(source)

            while q:
                x,parent = q.popleft()

                for j in adj[x]:
                    if j not in visited:
                        q.append((j,x))
                        visited.add(j)
                    elif parent != j:
                        hasCycle = True
        
        for u in range(n):
            if u not in visited:
                bfs(u)
                components += 1
        print(hasCycle, components)
        
        return not hasCycle and components == 1
        
            
            

