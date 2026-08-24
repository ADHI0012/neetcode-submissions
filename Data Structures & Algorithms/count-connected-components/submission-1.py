class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        components = 0
        q = collections.deque()
        visited = set()

        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        def bfs(i):
            visited.add(i)
            q.append(i)

            while q:
                x = q.popleft()

                for nei in adj[x]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)


        
        for i in range(n):
                if i not in visited:
                    bfs(i)
                    components += 1
        
        return components
        
        