class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        prefix_matrix = [[0] * cols for _ in range(rows)]
        req_sum = 0

        for i in range(rows):
            prefix_matrix[i][0] = self.matrix[i][0]

        for r in range(rows):
            for c in range(1, cols):
                prefix_matrix[r][c] = prefix_matrix[r][c-1] + self.matrix[r][c]

        for i in range(row1, row2 + 1):
            req_sum += prefix_matrix[i][col2]

            if col1 > 0:
                req_sum -= prefix_matrix[i][col1 - 1]

        return req_sum


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(self.matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)