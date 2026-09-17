class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0 for _ in range(n)]
        maxRight = [0 for _ in range(n)]
        res = 0

        maxLeft[0] = height[0]

        for i in range(1, n):
            maxLeft[i] = max(height[i], maxLeft[i - 1])
        
        maxRight[n - 1] = height[n - 1]

        for i in range(n - 2, -1, -1):
            maxRight[i] = max(height[i], maxRight[i + 1])

        
        for i in range(n):
            boundary = min(maxLeft[i], maxRight[i])
            res += max(boundary - height[i], 0)
        
        return res