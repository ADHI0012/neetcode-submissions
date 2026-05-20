class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        freqT = {}
        freqS = {}
        l = 0
        res, minLen = [-1, -1], float('inf')  

        for i in range(len(t)):
            freqT[t[i]] = 1 + freqT.get(t[i], 0)

        have, need = 0, len(freqT)

        for r in range(len(s)):
            ch = s[r]
            freqS[ch] = freqS.get(ch, 0) + 1

            if ch in freqT and freqT[ch] == freqS[ch]:
                have += 1

            while have == need:
                if r - l + 1 < minLen:
                    res = [l,r]
                    minLen = r - l + 1

                freqS[s[l]] -= 1

                if s[l] in freqT and freqT[s[l]] > freqS[s[l]]:
                    have -= 1
                l += 1

        
        L, R = res[0], res[1]
        return s[L:R+1] if minLen != float('inf') else ""
            