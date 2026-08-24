class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[0 for _ in range(n)] for _ in range(n)]
        components = 0
        q = collections.deque()
        visited = set()

        for i,j in edges:
            adj[i][j] = 1
            adj[j][i] = 1
        
        for i in range(n):
            adj[i][i] = 1
        
        def bfs(i):
            visited.add(i)
            q.append(i)

            while q:
                x = q.popleft()

                for j in range(n):
                    if adj[x][j] and j not in visited:
                        q.append(j)
                        visited.add(j)


        
        for i in range(n):
            for j in range(n):
                if adj[i][j] and i not in visited:
                    bfs(i)
                    components += 1
        
        return components
        
        