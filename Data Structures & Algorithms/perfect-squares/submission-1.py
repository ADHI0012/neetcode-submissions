class Solution:
    def numSquares(self, n: int) -> int:
        def perfect_squares(n):
            squares = []
            i = 1
            while i * i <= n:
                squares.append(i * i)
                i += 1
            return squares

        squares = perfect_squares(n)
        print(squares)
        dp = [float('inf') for _ in range(n + 1)]
        dp[0],dp[1] = 0,1

        if n < 2: return n

        for i in range(2, n + 1):
            for square in squares:
                if square <= i:
                    dp[i] = min(dp[i], 1 + dp[i - square])
        print(dp)
        return dp[n]
