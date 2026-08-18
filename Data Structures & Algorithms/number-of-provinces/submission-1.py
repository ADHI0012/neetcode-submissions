class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = len(isConnected)
        visited = set()
        provinces = 0
        q = collections.deque()


        def bfs(i):
            q.append(i)
            visited.add(i)
            while q:
                x = q.popleft()
                for j in range(len(isConnected[x])):
                    if isConnected[x][j] and j not in visited:
                        visited.add(j)
                        q.append(j)




        for i in range(cities):
            if i not in visited:
                bfs(i)
                provinces += 1


        return provinces