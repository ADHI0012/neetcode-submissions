class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []

        def checkValid(i,j):
            if j - i + 1 > 1 and s[i] == "0":
                return False
            if int(s[i:j+1]) > 255:
                return False
            return True

        def dfs(i, path):
            if i == len(s):
                if len(path) == 4:
                    res.append(".".join(path[:]))
                return
            
            for j in range(i, len(s)):
                if checkValid(i,j):
                    path.append(s[i:j+1])
                    dfs(j + 1, path)
                    path.pop()
        dfs(0,[])
        return res