class Solution:
    def findClosestElements(self, arr, k, x):
        res = []
        
        def binary_search(arr, target):
            l = 0
            r = len(arr) - 1

            while l <= r:
                mid = (l + r) // 2
                
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return l

        pos = binary_search(arr, x)

        left = pos - 1
        right = pos

        while len(res) != k:
            if left < 0:
                res.append(arr[right])
                right += 1
            elif right >= len(arr):
                res.append(arr[left])
                left -= 1

            else:
                if abs(arr[left] - x) > abs(arr[right] - x):
                    res.append(arr[right])
                    right += 1
                else:
                    res.append(arr[left])
                    left -= 1
        return sorted(res)
            
        
        
