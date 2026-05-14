from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        n = len(nums)
        res = []

        for i in range(k):
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])

        res.append(q[0])

        for i in range(n - k):
            if q[0] == nums[i]:
                q.popleft()

            while q and q[-1] < nums[i + k]:
                q.pop()
            q.append(nums[i + k])

            res.append(q[0])

        return res


        