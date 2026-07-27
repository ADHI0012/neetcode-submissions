class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1 for _ in range(n + 1)]
        def search(i):
            if i >= n:
                if i == n:
                    return 1
                return 0

            if cache[i] != -1:
                return cache[i]

            cache[i] = search(i + 1) + search(i + 2)
            return cache[i]

        return search(0)