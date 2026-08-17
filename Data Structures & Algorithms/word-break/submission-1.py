class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        wordDict = set(wordDict)

        lengths = set(len(word) for word in wordDict)

        for i in range(1, n + 1):
            for l in lengths:
                if l > i:
                    continue
                if dp[i - l] and s[i - l:i] in wordDict:
                    dp[i] = True

        return dp[n]

        