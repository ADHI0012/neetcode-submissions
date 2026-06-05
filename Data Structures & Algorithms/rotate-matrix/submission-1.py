class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        def reverse_array(arr):
            l,r = 0,len(arr) - 1
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l,r = l + 1, r - 1

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            reverse_array(matrix[i])
