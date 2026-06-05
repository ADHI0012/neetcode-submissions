class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        new_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

        i = 0

        for col in range(cols - 1, -1, -1):
            j = 0
            for row in range(rows):
                new_matrix[row][col] = matrix[i][j]
                j += 1
            i += 1

        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = new_matrix[i][j]
