from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        visited = set()
        rows, cols = len(image), len(image[0])


        def bfs(i, j):
            q.append((i, j))
            org_color = image[i][j]
            image[i][j] = color
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            while q:
                r, c = q.popleft()
                for m, n in directions:
                    row = r + m
                    col = c + n
                    if (row < 0 or col < 0 or row >= rows or col >= cols or (i, j) in visited or image[row][col] != org_color):
                        continue
                    
                    image[row][col] = color
                    visited.add((row, col))
                    q.append((row, col))

        
        bfs(sr, sc)
        return image

       

        
        