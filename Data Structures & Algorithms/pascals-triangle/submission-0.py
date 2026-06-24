class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        pascals = [[1], [1,1]]

        for i in range(2, numRows):
            row = [1 for _ in range(i + 1)]
            for j in range(1, i):
                row[j] = pascals[i - 1][j - 1] + pascals[i - 1][j]
            pascals.append(row)

        return pascals

        