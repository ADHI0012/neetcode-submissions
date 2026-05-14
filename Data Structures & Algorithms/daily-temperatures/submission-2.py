from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0 for _ in range(n)]
        q = deque()

        for i in range(n):
            
            while q and temperatures[q[-1]] < temperatures[i]:
                idx = q.pop()
                res[idx] = i - idx
            q.append(i)

        return res