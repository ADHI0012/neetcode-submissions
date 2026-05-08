class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        k = len(s1)

        if k > n:
            return False

        matchFreq = [0 for _ in range(26)]
        freq = [0 for _ in range(26)]

        for i in range(k):
            matchFreq[ord(s1[i]) - 97] += 1
            freq[ord(s2[i]) - 97] += 1

        for i in range(0,n-k):
            if freq == matchFreq:
                return True
            freq[ord(s2[i]) - 97] -= 1
            freq[ord(s2[i + k]) - 97] += 1

        return freq == matchFreq
            




        