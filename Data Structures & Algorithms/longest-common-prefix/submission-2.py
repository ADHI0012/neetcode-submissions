class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i in range(len(strs[0])):
            for s in strs:
                if len(s) == i:
                    return prefix
                if strs[0][i] != s[i]:
                    return prefix
            prefix += strs[0][i]

        return prefix

                    
        