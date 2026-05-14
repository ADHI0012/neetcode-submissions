class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr):
            l = 0
            r = len(arr) - 1

            while l <= r:
                mid = (l + r) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

            return False

        
        m = len(matrix) # rows
        n = len(matrix[0]) # columms

        l = 0
        r = m - 1

        while l <= r:
            mid = (l + r) // 2
            if binary_search(matrix[mid]):
                return True
            else:
                if matrix[mid][0] > target:
                    r = mid - 1
                else:
                    l = mid + 1

        return False